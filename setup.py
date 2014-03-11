# -*- coding: UTF-8 -*-
#
#    X I E R P A   3
#    OS X Application (c) 2014 buro@petr.com, www.petr.com, www.xierpa.com
#    Authors: Petr van Blokland, Michiel Kauw–A–Tjoe
#
#    No distribution without permission.
#
#    python setup.py py2app
#

from distutils.core import setup
import py2app
import os
from plistlib import readPlist, writePlist

appName = "Xierpa3App"

plist = dict(CFBundleIdentifier="com.petr.xierpa3app",
             LSMinimumSystemVersion="10.6.0",
             CFBundleShortVersionString="1.0.0",
             CFBundleVersion="1.0.0",
             CFBundleIconFile="icon.icns",)

dataFiles = ['Resources/English.lproj', ]
setup(data_files=dataFiles, app=[dict(script="Xierpa3App.py", plist=plist)],)

# correct the CFBundleIconFile
'''
infoPlistPath = os.path.join(os.path.dirname(__file__), "dist", "%s.app" % appName, "Contents", "Info.plist")
plist = readPlist(infoPlistPath)
plist["CFBundleIconFile"] = "icon.icns"
writePlist(plist, infoPlistPath)
'''
