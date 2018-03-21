# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.

# Code by Janosch Haber, University of Amsterdam. 2018

from parlai.core.params import ParlaiParser
from parlai.mturk.core.mturk_manager import MTurkManager
from parlai.mturk.tasks.dmg_pilot_mturk.worlds import MTurkDMGDialogWorld
from parlai.mturk.tasks.dmg_pilot_mturk.worlds import MTurkDMGDialogOnboardWorld
from parlai.mturk.tasks.dmg_pilot_mturk.worlds import MTurkDMGDialogWarmupWorld
from parlai.tasks.dmg_pilot_mturk.agents import DMGMultiRoundTeacher
from parlai.agents.local_human.local_human import LocalHumanAgent
import parlai.mturk.core.mturk_utils as mturk_utils
from parlai.core.agents import create_agent
from task_config import task_config
from copy import deepcopy

from collections import defaultdict
from random import randint
from copy import copy
import json
import os
import time


VERBOSE = True
game_id = None
worker_record = defaultdict(lambda: [])
worker_bans = []
available_games = None
worker_names = ["Avery", "Jordan", "Blake", "River", "Eden", "Phoenix", "Harley", "Alexis", "Parker", "Taylor"]


def main():
    """
    Main function for the DMG pilot data collection task
    :return: Nothing.
    """
    global available_games

    argparser = ParlaiParser(False, False)
    argparser.add_parlai_data_path()
    argparser.add_mturk_args()
    argparser.add_argument('--two_mturk_agents', dest='two_mturk_agents',
                           action='store_true', help='data collection mode '
                           'with converations between two MTurk agents')

    opt = argparser.parse_args()
    opt['task'] = 'dmg_pilot_dev'
    opt['datatype'] = 'dmg_pilot_data_1'
    opt.update(task_config)

    is_sandbox = True if opt['is_sandbox'] else False
    if is_sandbox: print("\n- - - Running in Sandbox Mode - - -")
    local_agent_1_id = 'local_1'
    mturk_agent_ids = ['mturk_agent_1']
    if opt['two_mturk_agents']:
        mturk_agent_ids.append('mturk_agent_2')

    mturk_manager = MTurkManager(
        opt=opt,
        mturk_agent_ids=mturk_agent_ids
    )
    mturk_manager.setup_server()

    # Remove qualification blocks
    # mturk_utils.delete_qualification('33DUYNETVPNVNFT4X22Z6F584M1WCM', is_sandbox)

    qual_name = 'DMG_Pilot_:_Max_Games_Reached_TEMP3'
    qual_desc = ('Qualification for a worker who completed the maximum number of games in the DMG Pilot')
    qualification_id = mturk_utils.find_or_create_qualification(qual_name, qual_desc, is_sandbox, True)
    print('Created qualification: ', qualification_id)

    available_games = len(DMGMultiRoundTeacher(opt=opt).episodes)
    print("Available games: {}".format(available_games))

    try:
        def load_records():
            global worker_record
            global worker_bans

            try:
                with open('records/worker_record.json', 'r') as infile:
                    worker_record = json.load(infile)
                    worker_record = defaultdict(list, worker_record)
                    print("Loaded worker records.")
            except FileNotFoundError:
                pass
            try:
                with open('records/worker_bans.json', 'r') as infile:
                    worker_bans = json.load(infile)
            except FileNotFoundError:
                pass

            # Exclude players who are banned by completing the maximum number of games in a previous HIT
            for worker_id in worker_bans:
                print("Excluded banned worker {}".format(worker_id))
                mturk_utils.give_worker_qualification(worker_id, qualification_id)

        def save_records():
            global worker_record
            global worker_bans

            if VERBOSE: print("Writing worker records to file")
            if not os.path.exists("records"):
                os.makedirs("records")
            with open('records/worker_record.json', 'w') as f:
                json.dump(worker_record, f)
            with open('records/worker_bans.json', 'w') as f:
                json.dump(worker_bans, f)

        def select_random_game(exceptions=None):
            """
            Returns a random game ID with exception of those specified in exceptions
            :param exceptions: list of game IDs that cannot be selected
            :return: a random game ID with exception of those specified in exceptions
            """
            global available_games

            while True:
                game_id = randint(0, available_games)
                # if VERBOSE: print("Game ID is {}. Exceptions are {}".format(game_id, exceptions))
                if exceptions is not None:
                    if game_id not in exceptions:
                        break
                else:
                    break
                # if VERBOSE: print("Selected random game {}".format(game_id))
            return game_id

        def game_is_blocked(id, player_id):
            """
            Returns True if the given game ID is blocked for the given player, False otherwise
            :param id: ID of a given game
            :param player_id: ID of a given player
            :return: True if the given game ID is blocked for the given player, False otherwise
            """
            if worker_record[player_id].count(id) == 2:
                return True
            else:
                return False

        def update_records(players, id):
            """
            Updates the HITs worker records
            :param players: players paired for a game
            :param id: game ID
            :return: Nothing.
            """
            global worker_record
            global worker_bans
            global game_id
            game_id = id

            # Add game ID to the worker record and to the blocked list if it is the second occurance.
            # If a player has played 10 games, he or she gets banned from the game.
            for player in players:
                player_id = player.worker_id
                worker_record[player_id].append(game_id)
                if len(worker_record[player_id]) == 5:
                    mturk_utils.give_worker_qualification(player_id, qualification_id)
                    worker_bans.append(player_id)

        def check_workers_eligibility(workers):
            """
            Checks the list of available workers, pairs the first two players that pass
            the game criteria and sets the corresponding game id
            :param workers: a list of all available workers
            :return: a list of two workers that are paired for the next game
            """
            global worker_record

            players = []
            # Return an empty list if not enough workers are in queue
            if len(workers) < 2:
                return players

            if VERBOSE: print("{} workers available:".format(len(workers)))

            for idx, worker in enumerate(workers):
                worker_id = worker.worker_id
                if VERBOSE: print("Worker: {}".format(worker_id))

                # Worker never played before. Pair him or her with the next queued worker who also never played before
                if worker_id not in worker_record.keys():
                    if VERBOSE: print("Worker has no recorded games")

                    for partner in workers[idx + 1:]:
                        partner_id = partner.worker_id
                        if partner_id not in worker_record.keys():
                            if VERBOSE: print("Partner: {}".format(partner_id))
                            players.append(worker)
                            players.append(partner)
                            next_game_id = select_random_game()
                            if VERBOSE: print(
                                "Partner has no recorded games. Setting game ID randomly to {}".format(next_game_id))
                            update_records(players, next_game_id)
                            return players

                    # Nobody in the queue is new. Continue with the loop
                    print("Nobody in the queue is new. Continue with the loop")
                    continue

                # Worker played before.
                else:
                    last_game_id = worker_record[worker_id][-1]
                    if not game_is_blocked(last_game_id, worker_id):
                        # Check if anybody in the queue has not played this game yet
                        for partner in workers[idx + 1:]:
                            partner_id = partner.worker_id
                            # If partner also played before, pair them
                            if partner_id in worker_record.keys() and last_game_id not in worker_record[partner_id]:
                                if VERBOSE: print("Partner has not played this game before.")
                                players.append(worker)
                                players.append(partner)
                                next_game_id = last_game_id
                                update_records(players, next_game_id)
                                return players

                    # No suitable partner was found to play worker's last game.
                    # So pair worker with the next available player and check their games
                    for partner in workers[idx + 1:]:
                        partner_id = partner.worker_id
                        # If partner also played before, pair them
                        if partner_id in worker_record.keys():
                            last_game_id = worker_record[partner_id][-1]
                            players.append(worker)
                            players.append(partner)
                            # Check if the partner's last game is not yet blocked and never played by the worker
                            if not game_is_blocked(last_game_id, partner_id) and last_game_id not in worker_record[
                                worker_id]:
                                next_game_id = last_game_id
                                if VERBOSE: print(
                                    "Partner has recorded games. Setting game ID to {}".format(next_game_id))
                                update_records(players, next_game_id)
                                return players
                            # Else select a random one that none of the two played before
                            else:
                                blocked = copy(worker_record[worker_id])
                                blocked.extend(worker_record[partner_id])
                                next_game_id = select_random_game(exceptions=blocked)
                                if VERBOSE: print(
                                    "Selected game {} as it was not played by any of the players before".format(
                                        next_game_id))
                                update_records(players, next_game_id)
                                return players

                                # Nobody in the queue played before. Continue with the loop

                    print("Nobody in the queue played before. Continue with the loop")
                    continue

            # No match could be made since the only workers available are from different categories
            print("No match could be made since the only workers available are from different categories")
            return players

        def get_worker_names(players):
            """
            Returns gender-neutral nicknames for the players based on how many games they played already
            :param players: List of player IDs
            :return: a list of gender-neutral nicknames for the players based on how many games they played already
            """
            global worker_names

            player_names = []
            for player in players:
                player_id = player.worker_id
                n = len(worker_record[player_id]) - 1
                print(n)
                player_names.append(worker_names[n])

            return player_names

        def assign_worker_roles(workers):
            """
            Assigns indexes to the assigned workers
            :param workers: list of workers
            :return: Nothing.
            """
            for index, worker in enumerate(workers):
                worker.id = mturk_agent_ids[index % len(mturk_agent_ids)]

        def save_conversation_duration(start_time):
            """
            Saves a conversation's duration to file
            :param start_time: Start time of the conversation
            :return: Nothing.
            """
            end_time = time.time()
            duration = end_time-start_time
            try:
                with open('records/durations.json', 'r') as infile:
                    durations = json.load(infile)
            except FileNotFoundError:
                durations = []

            durations.append(duration)

            if not os.path.exists("records"):
                os.makedirs("records")
            with open('records/durations.json', 'w') as f:
                json.dump(durations, f)

        def pay_workers(agents, get_pay):
            for agent in agents:
                if get_pay[agent.worker_id]:
                    print("Paying worker {}".format(agent.worker_id))
                    if len(worker_record[agents[0].worker_id]) > 1:
                        agent.pay_bonus(0.25, reason="DMP Pilot Bonus for multiple games")
                        agent.approve_work()
                        print("Paying bonus as well!")
                else:
                    print("Not paying agent {} as he or she disconnected (too early).".format(agent.worker_id))
                    agent.reject_work(reason='Disconnected before end of HIT')


        def run_conversation(mturk_manager, opt, workers):
            """
            Runs the conversation
            :param mturk_manager: MTurk manager
            :param opt: command line arguments
            :param workers: list of workers
            :return: Nothing.
            """
            global game_id
            global worker_record

            conversation_start_time = time.time()

            # Copy workers into agents list
            agents = workers[:]
            # Get worker names
            names = get_worker_names(agents)
            if names[0] == "Avery":
                names = ["Kelsey", "Robin"]
            print(names)

            # Create a local agent
            if not opt['two_mturk_agents']:
                if 'model' in opt:
                    local_agent = create_agent(opt)
                else:
                    local_agent = LocalHumanAgent(opt=None)

                local_agent.id = local_agent_1_id
                agents.append(local_agent)

            opt["batchindex"] = mturk_manager.started_conversations

            print("Loading game {}".format(game_id))

            # If the workers never played before, start with the warm-up round
            if len(worker_record[agents[0].worker_id]) == 1 and len(worker_record[agents[1].worker_id]) == 1:
                world = MTurkDMGDialogWarmupWorld(
                    opt=opt,
                    agents=agents,
                )
                if VERBOSE: print("--- Starting Warming-Up Round ---")
                while not world.episode_done():
                    if world.parley():
                        break

            world = MTurkDMGDialogWorld(
                opt=opt,
                agents=agents,
                game_id=game_id,
                names=names
            )

            log_timestamp = time.time()
            # Loop over all five rounds of the game
            get_pay = {agents[0]: False, agents[1]: False}
            for r in range(5):
                if VERBOSE: print("--- Starting round {} ---".format(r+1))

                if r == 0 and len(worker_record[agents[0].worker_id]) == 1 and len(worker_record[agents[1].worker_id]) == 1:
                    world.flush_buffer()

                disconnected = False
                while not world.episode_done():
                    if world.parley():
                        disconnected = True
                        break

                # Write the log data to file
                if VERBOSE: print("Logging data")
                world.round_log['round_nr'] = world.round_nr
                world.round_log['images'] = {world.player_labels[0]: world.data[world.player_labels[0]][world.round_nr],
                                             world.player_labels[1]: world.data[world.player_labels[1]][world.round_nr]}
                world.conversation_log['rounds'].append(deepcopy(world.round_log))

                if VERBOSE: print("Writing log to file")
                if not os.path.exists("logs"):
                    os.makedirs("logs")
                with open('logs/dmg_pilot_data_{}_{}.json'.format(world.assignment_ids[0], world.assignment_ids[1]), 'w') as f:
                    json.dump(copy(world.conversation_log), f)

                if disconnected:
                    if r > 2:
                        get_pay = world.conversation_log['disconnected']

                    world.shutdown()
                    if VERBOSE: print("Game ended due to disconnect.")
                    break

                if not r == 4:
                    # Reset the world for the next round
                    world.selections = defaultdict(lambda: dict())
                    world.round_log = world.reset_round_log()
                    world.turn_nr = -1
                    world.round_nr += 1
                    world.episodeDone = False

                    world.flush_buffer()

                else:
                    world.shutdown()
                    get_pay = {agents[0]: True, agents[1]: True}
                    if VERBOSE: print("Game ended.")

            save_conversation_duration(conversation_start_time)
            save_records()

            pay_workers(agents, get_pay)

            print("Conversation closed.")


        load_records()
        print("Loaded records.")

        def run_onboard(worker):
            global worker_record

            if worker.worker_id not in worker_record.keys():
                world = MTurkDMGDialogOnboardWorld(opt=opt, mturk_agent=worker)
                while not world.episode_done():
                    world.parley()
                world.shutdown()

        mturk_manager.set_onboard_function(onboard_function=run_onboard)

        mturk_manager.start_new_run()
        agent_qualifications = [{
            'QualificationTypeId': qualification_id,
            'Comparator': 'DoesNotExist',
            'RequiredToPreview': True
        }]
        mturk_manager.create_hits(qualifications=agent_qualifications)

        # Increasing restart time
        mturk_manager.ready_to_accept_workers(timeout_seconds = 120)

        eligibility_function = {
            'func': check_workers_eligibility,
            'multiple': True,
        }

        mturk_manager.start_task(
            eligibility_function=eligibility_function,
            assign_role_function=assign_worker_roles,
            task_function=run_conversation
        )

        if VERBOSE: print("HIT ended.")

    except BaseException:
        raise
    finally:
        mturk_manager.expire_all_unassigned_hits()
        mturk_manager.shutdown()


if __name__ == '__main__':
    main()