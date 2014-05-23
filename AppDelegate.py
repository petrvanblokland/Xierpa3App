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
from AppKit import NSObject #@UnresolvedImport
from PyObjCTools import AppHelper
from src.xierpa3window import Xierpa3Window
from twisted.internet import reactor

class XierpaAppDelegate(NSObject):
    u"""
    """

    def applicationShouldTerminate_(self, sender):
        if reactor.running:
            reactor.addSystemEventTrigger('after', 'shutdown', AppHelper.stopEventLoop)
            reactor.stop()
            return False
        return True

    def applicationDidFinishLaunching_(self, notification):
        reactor.interleave(AppHelper.callAfter)
        Xierpa3Window()

AppHelper.runEventLoop()
