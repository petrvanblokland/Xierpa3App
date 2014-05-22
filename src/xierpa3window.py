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
from xierpa3.sites.examples import HelloWorld, HelloWorldLayout, OneColumnSite, NavigationExample
from vanilla import RadioGroup, Window, Button
from constants import C

class Xierpa3Window(object):
    u"""
    Implementation of a vanilla-based GUI for the Xierpa 3 environment.
    """
    OPTIONS = [
        ("Hello world", HelloWorld),
        ("Hello world layout", HelloWorldLayout),
        ("One column", OneColumnSite),
        ("Navigation", NavigationExample),
    ]
    def __init__(self):
        u"""
        Initialize the window and open it.
        """
        self.w = Window((C.WINDOW_WIDTH, C.WINDOW_HEIGHT), "Xierpa 3",
                closable=True, minSize=(200, 200), maxSize=(1600, 1000))
        self.w.options = RadioGroup((10, 10, 150, 80), self.getOptionLabels(), callback=self.selectOptionCallback)
        self.w.run = Button((10, 100, 150, 24), 'Run', callback=self.runOptionCallback)
        self.w.open()

    def getOptionLabels(self):
        optionLabels = []
        for optionLabel, _ in self.OPTIONS:
            optionLabels.append(optionLabel)
        return optionLabels
            
    def selectOptionCallback(self, sender):
        _, optionClass = self.OPTIONS[sender.get()]
        
    def runOptionCallback(self, sender):
        _, optionClass = self.OPTIONS[self.w.options.get()]
        example = optionClass()
        example.run()
        