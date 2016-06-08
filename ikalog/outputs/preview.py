#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  IkaLog
#  ======
#  Copyright (C) 2015 Takeshi HASEGAWA
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import time

import cv2

# IkaOutput_Screen: IkaLog Output Plugin for Screen (video)
#


class Screen(object):

    last_update = 0

    def on_show_preview(self, context):
        img = context['engine'].get('preview', context['engine']['frame'])
        img_resized = cv2.resize(img, self.video_size)

        cv2.imshow('IkaLog', img_resized)

        r = None
        if (self.wait_ms == 0):
            now = time.time()
            if (now - self.last_update) > 2:
                r = cv2.waitKey(1)
                self.last_update = now
        else:
            r = cv2.waitKey(self.wait_ms)

        return r

    ##
    # Constructor
    # @param self         The Object Pointer.
    #
    def __init__(self, wait_ms=1, size=(1280, 720)):
        self.wait_ms = wait_ms
        self.video_size = size
        pass
