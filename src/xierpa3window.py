# -*- coding: UTF-8 -*-
#
#    X I E R P A   3
#    OS X Application (c) 2014 buro@petr.com, www.petr.com, www.xierpa.com.
#    Authors: Petr van Blokland, Michiel Kauw–A–Tjoe.
#
#    No distribution without permission.
#

import vanilla
from constants import Constants

class Xierpa3Window(Constants):
    u"""
    Implementation of a vanilla-based GUI for the Xierpa 3 environment.
    """

    def __init__(self):
        u"""
        Initialize the window and open it.
        """
        self.paths = []
        options = ["Xierpa 3 Server", "HTML + Sass", "Kirby Template", "WordPress Template"]
        self.w = vanilla.Window((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), "Xierpa 3", closable=True)
        self.w.radioGroup = vanilla.RadioGroup((10, 10, -10, 80),
                                options,
                                callback=self.radioGroupCallback)
        self.w.open()

    def radioGroupCallback(self, sender):
        print "radio group edit!", sender.get()
