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
#    xierpa3app.py
#
import webbrowser
from constants import C
from vanilla import RadioGroup, Window, Button, CheckBox
from xierpa3.sites.doingbydesign.doingbydesign import DoingByDesign
from xierpa3.sites.examples import HelloWorld, HelloWorldLayout, OneColumnSite

class Xierpa3App(object):
    u"""Implementation of a vanilla-based GUI for the Xierpa 3 environment."""
    
    PORT = 8060
    URL = 'http://localhost:%d' % PORT
    
    SITE_LABELS = [
        ("Hello world", HelloWorld()),
        ("Hello world layout", HelloWorldLayout()),
        ("One column", OneColumnSite()),
        ("DoingByDesign", DoingByDesign()),
    ]        
    def __init__(self):
        u"""
        Initialize the window and open it.
        """
        self.w = Window((C.WINDOW_WIDTH, C.WINDOW_HEIGHT), "Xierpa 3",
            closable=True, minSize=(200, 200), maxSize=(1600, 1000))
        self.w.optionalSites = RadioGroup((10, 10, 150, 100), self.getSiteLabels(), callback=self.selectSiteCallback)
        self.w.run = Button((10, 140, 150, 24), 'Open', callback=self.openSiteCallback)
        self.w.forceCss = CheckBox((180, 10, 150, 24), 'Force make CSS')
        self.w.open()

    def getSiteLabels(self):
        siteLabels = []
        for siteLabel, _ in self.SITE_LABELS:
            siteLabels.append(siteLabel)
        return siteLabels
            
    def selectSiteCallback(self, sender):
        pass
        
    def openSiteCallback(self, sender):
        url = self.URL
        if self.w.forceCss.get():
            url += '/force'
        webbrowser.open(url)

    def getSite(self):
        _, site = self.SITE_LABELS[self.w.optionalSites.get()]
        return site
    