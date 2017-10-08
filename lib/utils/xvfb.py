# -*- coding: utf-8 -*-
from xvfbwrapper import Xvfb

class Xvfb(object):
    vdisplay = Xvfb()

    @classmethod
    def start(cls):
        cls.vdisplay.start()

    @classmethod
    def stop(cls):
        cls.vdisplay.stop()
