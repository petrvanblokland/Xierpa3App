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
from vanilla import RadioGroup, Window, Button, CheckBox, EditText
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
        siteLabels = self.getSiteLabels()
        y = len(siteLabels)*20
        self.w.optionalSites = RadioGroup((10, 10, 150, y), siteLabels, 
            callback=self.selectSiteCallback, sizeStyle='small')
        self.w.openSite = Button((10, y+20, 150, 20), 'Open site', callback=self.openSiteCallback, sizeStyle='small')
        self.w.openCss = Button((10, y+45, 150, 20), 'Open CSS', callback=self.openCssCallback, sizeStyle='small')
        self.w.makeSite = Button((10, y+70, 150, 20), 'Make site', callback=self.makeSiteCallback, sizeStyle='small')
        self.w.forceCss = CheckBox((180, 10, 150, 20), 'Force make CSS', sizeStyle='small')
        self.w.console = EditText((10, -200, -10, -10), sizeStyle='small')
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

    def openCssCallback(self, sender):
        url = self.URL
        if self.w.forceCss.get():
            url += '/force'
        webbrowser.open(url + '/css/style.css')

    def makeSiteCallback(self, sender):
        _, site = self.SITE_LABELS[self.w.optionalSites.get()]
        site.make()
        
    def getSite(self):
        _, site = self.SITE_LABELS[self.w.optionalSites.get()]
        return site
    
    def handleRequest(self, httprequest, site):
        self.addConsole(`httprequest` + ' ' + `site.e.form`)
        
    def addConsole(self, s):
        self.w.console.set(self.w.console.get() + '\n' + s)
        
    