# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#    xierpa server
#    Copyright (c) 2014+  buro@petr.com, www.petr.com, www.xierpa.com
#    
#    X I E R P A  3  A P P
#    Distribution by the MIT License.
#
# -----------------------------------------------------------------------------
#
#    xierpa3window.py
#
import vanilla
from constants import C

class Xierpa3Window(object):
    u"""
    Implementation of a vanilla-based GUI for the Xierpa 3 environment.
    """

    def __init__(self):
        u"""
        Initialize the window and open it.
        """
        self.w = vanilla.Window((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), "Xierpa 3",
                                closable=True, minSize=(200, 200), maxSize=(1600, 1000))
        self.w.templates = self.getXierpa3Options()
        self.w.open()


    def getXierpa3Options(self):
        options = ["Xierpa 3 Server", "HTML + Sass", "Kirby Template", "WordPress Template"]
        return vanilla.RadioGroup((10, 10, -10, 80), options, callback=self.radioGroupCallback)

    def radioGroupCallback(self, sender):
        print "radio group edit!", sender.get()

