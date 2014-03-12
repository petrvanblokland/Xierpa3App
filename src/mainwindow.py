# -*- coding: UTF-8 -*-
#
#    X I E R P A   3
#    OS X Application (c) 2014 buro@petr.com, www.petr.com, www.xierpa.com.
#    Authors: Petr van Blokland, Michiel Kauw–A–Tjoe.
#
#    No distribution without permission.
#

from vanilla import *

import os
import httplib, mimetypes, urllib, binascii
from xierpalib.tools.parsers.json import cjson

from drop import Drop
from constants import Constants

class MainWindow(Constants):
    u"""
    Implementation of a vanilla-based upload GUI for the Xierpa environment.
    TODO: enable password, encryption via SSH keys.
    """

    def __init__(self):
        u"""
        Initialize the window and open it.
        """
        self.paths = []
        self.w = Window((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), "Xierpa 3", closable=False)
        self.w.open()