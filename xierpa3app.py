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

class SimpleAppAppDelegate(NSObject):

    def applicationDidFinishLaunching_(self, notification):
        Xierpa3Window()

if __name__ == "__main__":
    # Bring app to top
    #NSApp.activateIgnoringOtherApps_(True)

    AppHelper.runEventLoop()
