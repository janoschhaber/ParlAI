# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.

# Code by Janosch Haber, University of Amsterdam. 2018

import parlai.core.build_data as build_data
import os

def build(opt):
    dpath = os.path.join(opt['datapath'], 'dmg_pilot')
    version = '1'

    if not build_data.built(dpath, version_string=version):
        print('[building data: ' + dpath + ']')

        # make a clean directory if needed
        if build_data.built(dpath):
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # Download the data from github
        fname = 'coco_selection.zip'
        # url = ('https://raw.githubusercontent.com/janoschhaber/psivgd/166953fd1a5c15d1b164fcf1fcafe28e87440e0c/coco_selection.zip')
        url = 'https://raw.githubusercontent.com/janoschhaber/psivgd/d4ebee8de4b241d89d8ad7acaf7d21a2bd062573/dmg_pilot_mturk.zip'
        print('[downloading data from: ' + url + ']')
        build_data.download(url, dpath, fname)
        build_data.untar(dpath, fname)

        # Mark as done
        build_data.mark_done(dpath, version_string=version)
