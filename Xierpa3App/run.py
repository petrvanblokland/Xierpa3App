# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#     BuroFont Editor
#     (c) 2014+  Font Bureau
#
#     No distribution without permission.
#
# -----------------------------------------------------------------------------
#
#   run.py
#
#   http://twistedmatrix.com/documents/13.0.0/api/twisted.internet._threadedselect.html
#
#
import os
from PyObjCTools import AppHelper
from AppKit import NSApplication, NSApp, NSBundle, NSLog # @UnresolvedImport
import objc
objc.setVerbose(True) # @UndefinedVariable

# Specialized reactor for integrating with arbitrary foreign event loop, such as those you find in GUI toolkits.
from twisted.internet._threadedselect import install
reactor = install()

# import modules containing classes required to start application and load MainMenu.nib
import XierpaAppDelegate

app = NSApplication.sharedApplication()
nibPath = os.path.join(os.path.dirname(__file__), "dist", "Xierpa 3.app", "Contents", "Resources", "en.lproj", "MainMenu.nib")
NSBundle.loadNibFile_externalNameTable_withZone_(nibPath, {}, None) # @UndefinedVariable
delegate = XierpaAppDelegate.XierpaAppDelegate.alloc().init() # @UndefinedVariable
app.setDelegate_(delegate)

# Bring app to top
NSApp.activateIgnoringOtherApps_(True)

AppHelper.runEventLoop()
