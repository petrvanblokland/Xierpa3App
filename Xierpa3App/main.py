from PyObjCTools import AppHelper

# Specialized reactor for integrating with arbitrary foreign event loop, such as those you find in GUI toolkits.
from twisted.internet._threadedselect import install
reactor = install()

import XierpaAppDelegate #@UnusedImport

AppHelper.runEventLoop()
