# -*- coding: UTF-8 -*-
#
#    X I E R P A   3
#    OS X Application (c) 2014 buro@petr.com, www.petr.com, www.xierpa.com
#    Authors: Petr van Blokland, Michiel Kauw–A–Tjoe
#
#    No distribution without permission.
#

from AppKit import NSObject # , NSColor, NSView, NSFilenamesPboardType, NSDragOperationNone, NSDragOperationCopy
from PyObjCTools import AppHelper

from mainwindow import MainWindow

class SimpleAppAppDelegate(NSObject):

    def applicationDidFinishLaunching_(self, notification):
        MainWindow()

if __name__ == "__main__":
    AppHelper.runEventLoop()
