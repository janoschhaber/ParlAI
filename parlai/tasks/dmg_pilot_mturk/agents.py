# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.

# Code by Janosch Haber, University of Amsterdam. 2018

from parlai.core.teachers import Teacher
from .build import build
import random
import json
import os

WELCOME_MESSAGE = ('Round {} \nPlayer {}, you see the following images:\n{}'
                   'Find out which ones are also shown to the other player and which ones are different.')
EOS_TOKEN = '<eos>'
SELECTION_TOKEN = '<selection>'

DIF_TOKEN = '<dif>'
COM_TOKEN = '<com>'

NEXT_ROUND_TOKEN = '<next_round>'
FEEDBACK_TOKEN = '<feedback>'

YOU_TOKEN = 'YOU:'
THEM_TOKEN = 'THEM:'


class DMGMultiRoundTeacher(Teacher):

    def __init__(self, opt, shared=None):
        super().__init__(opt, shared)
        self.datatype = opt['datatype'].split(':')[0]
        filename = 'dmg_pilot_mturk_games'
        self.random = self.datatype == filename
        build(opt)
        data_path = os.path.join(opt['datapath'], 'dmg_pilot', 'dmg_pilot_mturk', filename + '.json')

        if shared and 'data' in shared:
            self.episodes = shared['episodes']
        else:
            self._setup_data(data_path)

        # for ordered data in batch mode (especially, for validation and testing), 
        # each teacher in the batch gets a start index and a step size so they all process disparate sets of the data
        self.step_size = opt.get('batchsize', 1)
        self.data_offset = opt.get('batchindex', 0)

        super().reset()
        self.episode_idx = self.data_offset - self.step_size
        self.dialogue_idx = None
        self.expected_response = None
        self.epochDone = False     

    def share(self):
        shared = super().share()
        shared['episodes'] = self.episodes
        return shared

    def _setup_data(self, data_path):
        print('Loading: ' + data_path)
        with open(data_path, 'r') as data:
            self.episodes = json.load(data)

    def observe(self, observation):
        if self.expected_response is not None:
            self.metrics.update(observation, self.expected_response)
            self.expected_response = None
        return observation

    def act(self):
        if self.dialogue_idx is not None:
            # continue existing conversation
            return self._continue_dialogue()
        elif self.random:
            # if random, then select the next random example
            self.episode_idx = random.randrange(len(self.episodes))
            return self._start_dialogue()
        elif self.episode_idx + self.step_size >= len(self.episodes):
            # end of examples
            self.epochDone = True
            return {'episode_done': True}
        else:
            # get next non-random example
            self.episode_idx = (self.episode_idx + self.step_size) % len(self.episodes)
            return self._start_dialogue()

    def setup_data(self, path):
        pass


class DefaultTeacher(DMGMultiRoundTeacher):
    pass
