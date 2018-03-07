# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.

# Code by Janosch Haber, University of Amsterdam. 2018

from parlai.mturk.core.worlds import MTurkTaskWorld
from parlai.core.worlds import validate
from parlai.tasks.dmg_pilot_mturk.agents import DMGMultiRoundTeacher
from parlai.tasks.dmg_pilot_mturk.agents import WELCOME_MESSAGE
from parlai.tasks.dmg_pilot_mturk.agents import SELECTION_TOKEN
from parlai.tasks.dmg_pilot_mturk.agents import COM_TOKEN
from parlai.tasks.dmg_pilot_mturk.agents import DIF_TOKEN
from parlai.tasks.dmg_pilot_mturk.agents import NEXT_ROUND_TOKEN
from parlai.tasks.dmg_pilot_mturk.agents import FEEDBACK_TOKEN

from joblib import Parallel, delayed
from copy import deepcopy
from collections import defaultdict
from numpy import random as nprand
import random
import time

VERBOSE = True


class MTurkDMGDialogWorld(MTurkTaskWorld):

    def __init__(self, opt, agents=None, game_id=0, names=("Kelsey", "Robin"), shared=None):
        order = nprand.permutation(len(agents))
        shuffled_agents = [agents[i] for i in order]
        shuffled_names = [names[i] for i in order]
        self.agents = shuffled_agents
        self.names = shuffled_names

        self.acts = [None] * len(agents)
        self.task = DMGMultiRoundTeacher(opt=opt)
        self.game_id = game_id
        self.round_nr = -1
        self.turn_nr = -1
        self.players = [agents[0].id, agents[1].id]
        self.player_labels = ["A", "B"]
        self.selections = defaultdict(lambda: dict())
        self.data = None
        self.common = None
        self.episodeDone = False
        self.doneCounter = 0
        self.rounds_random = nprand.permutation(5)
        self.last_agent = None

        self.conversation_log = {
            'game_id': self.game_id,
            'players': self.players,
            'agent_labels': self.player_labels,
            'agent_ids' :[],
            'rounds': [],
            'feedback': {}
        }

        for i, agent in enumerate(agents):
            try:
                self.conversation_log['agent_ids'].append(agent.worker_id)
            except:
                self.conversation_log['agent_ids'].append(self.player_labels[i])
        self.round_log = self.reset_round_log()

        if VERBOSE: print("Game ID is {}".format(game_id))

    def parley(self):
        """
        Main communication loop for the agents involved in the task
        :return: Nothing
        """

        print("PARLEY!")
        # If a new round has started, load the game data (if necessary) and send it to the players
        if self.turn_nr == -1:
            print("Loading Data ot MTurk")
            # Load a new game (data) if no game is running yet
            if self.round_nr == -1 and not self.data:
                self.data = self.task.episodes[self.game_id % len(self.task.episodes)]
                self.round_nr = 0

            # Determine the common images
            self.common = list(set(self.data[self.player_labels[0]][self.rounds_random[self.round_nr]])
                               .intersection(self.data[self.player_labels[1]][self.rounds_random[self.round_nr]]))

            # Send a welcome message with the game data to all players
            counter = 0
            for agent, player, player_label in zip(self.agents, self.players, self.player_labels):

                image_list = ""
                for image in self.data[player_label][self.rounds_random[self.round_nr]]:
                    image_list += "{} \n".format(image)

                action = {}
                action['text'] = WELCOME_MESSAGE.format(self.round_nr+1, player, image_list)
                action['images'] = self.data[player_label][self.rounds_random[self.round_nr]]
                action['name'] = self.names[counter]
                if VERBOSE: print("Worker {} name: {}".format(player, action['name']))
                if VERBOSE: print("Your images are: {}".format(action['images']))
                agent.observe(validate(action))
                counter += 1

            self.turn_nr += 1

        # Else observe the actions of the players
        else:
            for agent, player, player_label in zip(self.agents, self.players, self.player_labels):

                if self.episodeDone:
                    print("Episode done!")
                    break

                print("Entering regular dialogue mode")
                while True:
                    # Obtain the action of a MTurk agent
                    try:
                        action = agent.act(timeout=None)
                    # Obtain the action of a local agent
                    except TypeError:
                        action = agent.act()

                    is_done = self.parse_action(agent, player, player_label, action)
                    if is_done: break

                self.last_agent = agent

        self.turn_nr += 1


    def parse_action(self, agent, player, player_label, action):
        # Parse a selection
        message = action["text"]
        if VERBOSE: print("Agent {} sent : {}".format(player, message))

        # Log the message
        log_entry = self.create_message_log_entry(agent, player, player_label, message)
        self.round_log['messages'].append(log_entry)
        message = message.split(" ")

        # Message is a selection. Parse it
        if message[0] == SELECTION_TOKEN:
            try:
                assert len(message) == 3
                image_id = message[-1]
                image_type = message[1]
                self.selections[agent][image_id] = image_type
                if VERBOSE: print("Agent {} marked image {} as {}".format(player, image_id, image_type))

            except:
                print("WARNING: Your selection could not be parsed properly!")

        # Player requests feedback. Check if round is completed and provide it
        elif message[0] == FEEDBACK_TOKEN:
            if self.all_selected():
                scores = self.send_feedback()
                self.round_log['score'] = scores
                return True
            else:
                agent.observe(validate({'text': "<hint>"}))

        # Player wants to move to the next round. Check if the previous round is finished
        # and wait for second player
        elif message[0] == NEXT_ROUND_TOKEN and self.all_selected() and self.doneCounter == 0:
            if VERBOSE: print("One player clicked continue")

            # If it was the last round and the player gave feedback, save it to the log
            try:
                feedback = "".join(message[1:])
                self.conversation_log['feedback'][player_label] = feedback
            except:
                pass

            self.doneCounter += 1
            return True

        # Second player also wants to continue. Check if the previous round is finished and continue
        elif message[0] == NEXT_ROUND_TOKEN and self.all_selected() and self.doneCounter == 1:

            # If it was the last round and the player gave feedback, save it to the log
            try:
                feedback = "".join(message[1:])
                self.conversation_log['feedback'][player_label] = feedback
            except:
                pass

            if VERBOSE: print("Logging data")
            self.round_log['round_nr'] = self.round_nr
            self.round_log['images'] = {self.player_labels[0]: self.data[self.player_labels[0]][self.round_nr],
                                        self.player_labels[1]: self.data[self.player_labels[1]][self.round_nr]}
            self.conversation_log['rounds'].append(deepcopy(self.round_log))

            self.doneCounter = 0
            self.episodeDone = True
            if VERBOSE: print("Done.")
            return True

        # Regular text message. Display it to the other players and break the while loop
        elif not action['episode_done']:
            # Let the other agents observe the action
            for other_agent in self.agents:
                if other_agent != agent:
                    other_agent.observe(validate(action))
            return True

        # Check if episode ended due to disconnection or timeout or a returned HIT
        else:
            self.episodeDone = True
            print("RECEIVED A DISCONNECT ERROR!")
            return True

        return False

    def send_feedback(self):
        """
        Sends feedback to the player after each round of the game and calculates the scores
        :return: The scores for all players. 6 points means all images marked correctly, 0 points means zero correct.
        """
        # if VERBOSE: print("The common images were {}".format(self.common))

        scores = {self.players[0]: 0, self.players[1]: 0}

        # Send a feedback message to all players
        for agent, player in zip(self.agents, self.players):

            solutions = []

            feedback = "Feedback for Agent {}:\n".format(player)
            for image_id, selection in self.selections[agent].items():
                # file = "person_fridge_pilot/COCO_train2014_{:0>12d}.jpg".format(int(image_id))
                file = image_id
                feedback += "You marked image {} as ".format(image_id)
                if selection == COM_TOKEN: feedback += "common"
                elif selection == DIF_TOKEN: feedback += "different"
                feedback += " which was "
                if (selection == COM_TOKEN and file in self.common) \
                        or (selection == DIF_TOKEN and file not in self.common):
                    feedback += "correct.\n"
                    solutions.append([image_id, 1])
                    scores[player] += 1
                else:
                    feedback += "incorrect.\n"
                    solutions.append([image_id, 0])

            try:
                assert len(solutions) == 6
            except:
                print("Not all images marked yet!")
                continue

            action = {}
            action['text'] = feedback
            action['solution'] = solutions
            if VERBOSE: print(action['solution'])
            agent.observe(validate(action))

        print("Scores for this round are {}".format(scores))
        return scores

    def create_message_log_entry(self, agent, player, player_label, message):

        try:
            agent_id = agent.worker_id
        except:
            agent_id = player_label

        entry = {
            'timestamp': time.time(),
            'turn': self.turn_nr,
            'speaker': player_label,
            'agent_label': player,
            'agent_id': agent_id,
            'message': message
        }
        return entry

    def all_selected(self):
        """
        Returns True if all players selected all images
        :return: True if all players selected all images
        """
        for agent in self.agents:
            if len(self.selections[agent]) < 6:
                return False
        return True

    def reset_round_log(self):
        """
        Resets the log's game round entry dict
        :return: An empty game round entry dict
        """
        return {
            'round_nr': None,
            'score': None,
            'images': None,
            'messages': []
        }

    def episode_done(self):
        """
        Returns True if the current game round (episode) is done
        :return: True if the current game round (episode) is done
        """
        return self.episodeDone

    def set_game_id(self, id):
        """
        Sets the game id
        :param id: game id to use for the next game
        :return: Nothing.
        """
        self.game_id = id

    def flush_buffer(self):
        agents_done = [False for _ in self.agents]
        while sum(agents_done) < len(self.agents):
            for idx, agent in enumerate(self.agents):
                if not agents_done[idx] and agent.act(blocking=False) is not None:
                    agent.observe(validate({'text': '<buffer>'}))
                    agents_done[idx] = True
            time.sleep(0.1)

    def shutdown(self):
        """
        Shuts down all mturk agents in parallel
        (if one mturk agent is disconnected then it could prevent other mturk agents from completing.)
        """
        global shutdown_agent

        def shutdown_agent(agent):
            # Shut down MTurk agents
            try:
                agent.shutdown(timeout=None)
            # Shut down local agents
            except Exception:
                agent.shutdown()

        Parallel(n_jobs=len(self.agents), backend='threading')\
            (delayed(shutdown_agent)(agent) for agent in self.agents)


class MTurkDMGDialogOnboardWorld(MTurkTaskWorld):

    def __init__(self, opt, agents=None, names=("Kelsey", "Robin"), shared=None):
        order = nprand.permutation(len(agents))
        shuffled_agents = [agents[i] for i in order]
        shuffled_names = [names[i] for i in order]
        self.agents = shuffled_agents
        self.names = shuffled_names
        self.episodeDone = False
        self.selections = defaultdict(lambda: dict())

        self.data = {"A": ["person_donut/COCO_train2014_000000490481.jpg",
                           "person_donut/COCO_train2014_000000011282.jpg",
                           "person_donut/COCO_train2014_000000117884.jpg"],
                     "B": ["person_donut/COCO_train2014_000000490481.jpg",
                           "person_donut/COCO_train2014_000000117884.jpg",
                           "person_donut/COCO_train2014_000000399480.jpg"]}

        self.common = ["person_donut/COCO_train2014_000000490481.jpg",
                       "person_donut/COCO_train2014_000000117884.jpg"]

        self.players = [agents[0].id, agents[1].id]
        self.player_labels = ["A", "B"]

        self.turn_nr = -1
        self.doneCounter = 0

    def parley(self):
        # If a new round has started, load the game data (if necessary) and send it to the players
        if self.turn_nr == -1:
            # Send a welcome message with the game data to all players
            counter = 0
            for agent, player, player_label in zip(self.agents, self.players, self.player_labels):

                image_list = ""
                for image in self.data[player_label]:
                    image_list += "{} \n".format(image)

                action = {}
                action['text'] = "<warm-up> Warming-up game"
                action['images'] = self.data[player_label]
                action['name'] = self.names[counter]
                if VERBOSE: print("Worker {} name: {}".format(player, action['name']))
                if VERBOSE: print("Your images are: {}".format(action['images']))
                agent.observe(validate(action))
                counter += 1

            self.turn_nr += 1

        # Else observe the actions of the players
        else:
            for agent, player, player_label in zip(self.agents, self.players, self.player_labels):

                if self.episodeDone:
                    print("Episode done!")
                    break

                print("Entering regular dialogue mode")
                while True:
                    # Obtain the action of a MTurk agent
                    try:
                        action = agent.act(timeout=None)
                    # Obtain the action of a local agent
                    except TypeError:
                        action = agent.act()

                    is_done = self.parse_action(agent, player, player_label, action)
                    if is_done: break

        self.turn_nr += 1

    def parse_action(self, agent, player, player_label, action):# Parse a selection
        message = action["text"]
        if VERBOSE: print("Agent {} sent : {}".format(player, message))
        message = message.split(" ")

        # Message is a selection. Parse it
        if message[0] == SELECTION_TOKEN:
            try:
                assert len(message) == 3
                image_id = message[-1]
                image_type = message[1]
                self.selections[agent][image_id] = image_type
                if VERBOSE: print("Agent {} marked image {} as {}".format(player, image_id, image_type))

            except:
                print("WARNING: Your selection could not be parsed properly!")

        # Player requests feedback. Check if round is completed and provide it
        elif message[0] == FEEDBACK_TOKEN:
            if self.all_selected():
                _ = self.send_feedback()
                return True

            else:
                agent.observe(validate({'text': "<hint>"}))

        # Player wants to move to the next round. Check if the previous round is finished
        # and wait for second player
        elif message[0] == NEXT_ROUND_TOKEN and self.all_selected() and self.doneCounter == 0:
            if VERBOSE: print("One player clicked continue")

            self.doneCounter += 1
            return True

        # Second player also wants to continue. Check if the previous round is finished and continue
        elif message[0] == NEXT_ROUND_TOKEN and self.all_selected() and self.doneCounter == 1:

            self.doneCounter = 0
            self.episodeDone = True
            return True

        # Regular text message. Display it to the other players and break the while loop
        elif not action['episode_done']:
            # Let the other agents observe the action
            for other_agent in self.agents:
                if other_agent != agent:
                    other_agent.observe(validate(action))

            return True

        # Check if episode ended due to disconnection or timeout or a returned HIT
        else:
            self.episodeDone = True
            return True

    def flush_buffer(self):
        agents_done = [False for _ in self.agents]
        while sum(agents_done) < len(self.agents):
            for idx, agent in enumerate(self.agents):
                if not agents_done[idx] and agent.act(blocking=False) is not None:
                    agent.observe(validate({'text': '<buffer>'}))
                    agents_done[idx] = True
            time.sleep(0.1)

    def send_feedback(self):
        """
        Sends feedback to the player after each round of the game and calculates the scores
        :return: The scores for all players. 6 points means all images marked correctly, 0 points means zero correct.
        """
        # if VERBOSE: print("The common images were {}".format(self.common))

        scores = {self.players[0]: 0, self.players[1]: 0}

        # Send a feedback message to all players
        for agent, player in zip(self.agents, self.players):

            solutions = []

            feedback = "Feedback for Agent {}:\n".format(player)
            for image_id, selection in self.selections[agent].items():
                # file = "person_fridge_pilot/COCO_train2014_{:0>12d}.jpg".format(int(image_id))
                file = image_id
                feedback += "You marked image {} as ".format(image_id)
                if selection == COM_TOKEN: feedback += "common"
                elif selection == DIF_TOKEN: feedback += "different"
                feedback += " which was "
                if (selection == COM_TOKEN and file in self.common) \
                        or (selection == DIF_TOKEN and file not in self.common):
                    feedback += "correct.\n"
                    solutions.append([image_id, 1])
                    scores[player] += 1
                else:
                    feedback += "incorrect.\n"
                    solutions.append([image_id, 0])

            try:
                assert len(solutions) == 3
            except:
                print("Not all images marked yet!")
                continue

            action = {}
            action['text'] = feedback
            action['solution'] = solutions
            if VERBOSE: print(action['solution'])
            agent.observe(validate(action))

        print("Scores for this round are {}".format(scores))
        return scores

    def all_selected(self):
        """
        Returns True if all players selected all images
        :return: True if all players selected all images
        """
        for agent in self.agents:
            if len(self.selections[agent]) < 3:
                return False
        return True

    def episode_done(self):
        """
        Returns True if the current game round (episode) is done
        :return: True if the current game round (episode) is done
        """
        return self.episodeDone
