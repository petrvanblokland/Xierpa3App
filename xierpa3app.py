# -*- coding: UTF-8 -*-
#
#    X I E R P A   3
#    OS X Application (c) 2014 buro@petr.com, www.petr.com, www.xierpa.com.
#    Authors: Petr van Blokland, Michiel Kauw–A–Tjoe.
#
#    No distribution without permission.
#

'''
NSColor, NSView, NSFilenamesPboardType, NSDragOperationNone, NSDragOperationCopy
'''
from AppKit import NSObject, NSApp
from PyObjCTools import AppHelper
from src.xierpa3window import Xierpa3Window

class SimpleAppAppDelegate(NSObject):

    def applicationDidFinishLaunching_(self, notification):
        Xierpa3Window()

if __name__ == "__main__":
    # Bring app to top
    #NSApp.activateIgnoringOtherApps_(True)

    AppHelper.runEventLoop()
