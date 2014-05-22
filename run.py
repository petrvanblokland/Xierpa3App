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
#
import os
from PyObjCTools import AppHelper
from AppKit import NSApplication, NSApp, NSBundle, NSLog # @UnresolvedImport
import objc
objc.setVerbose(True) # @UndefinedVariable

def writeToLog(message):
    import logging
    logging.basicConfig(filename=os.path.expanduser('~/example.log'),level=logging.DEBUG)
    log = logging.getLogger()
    log.exception(message)

def postMortem():
    import pdb
    pdb.post_mortem()

def cocoaLog(message):
    NSLog(message)

def printTraceback():
    import traceback
    print traceback.format_exc()

try:
    # import modules containing classes required to start application and load MainMenu.nib
    import AppDelegate
except Exception, e:
    message = "Error running BuroFont application, %s" % e
    cocoaLog(message)
    writeToLog(message)
    printTraceback()
    postMortem()

app = NSApplication.sharedApplication()
nibPath = os.path.join(os.path.dirname(__file__), "dist", "BuroFont.app", "Contents", "Resources", "en.lproj", "MainMenu.nib")
NSBundle.loadNibFile_externalNameTable_withZone_(nibPath, {}, None) # @UndefinedVariable
delegate = AppDelegate.XierpaAppDelegate.alloc().init() # @UndefinedVariable
app.setDelegate_(delegate)

# Bring app to top
NSApp.activateIgnoringOtherApps_(True)

AppHelper.runEventLoop()
