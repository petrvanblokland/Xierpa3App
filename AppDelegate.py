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
from src.xierpa3app import Xierpa3App
from src.client import Client
from twisted.internet import reactor
from twisted.web import server

class XierpaAppDelegate(NSObject):
    u"""
    """

    def applicationShouldTerminate_(self, sender):
        if reactor.running: #@UndefinedVariable
            reactor.addSystemEventTrigger('after', 'shutdown', AppHelper.stopEventLoop) #@UndefinedVariable
            reactor.stop() #@UndefinedVariable
            return False
        return True

    def applicationDidFinishLaunching_(self, notification):
        client = Client()
        client.app = Xierpa3App()
        site = server.Site(client)
        reactor.interleave(AppHelper.callAfter) #@UndefinedVariable
        reactor.listenTCP(8060, site) # @UndefinedVariable

AppHelper.runEventLoop()
