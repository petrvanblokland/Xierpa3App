from PyObjCTools import AppHelper

from AppKit import NSImage, NSBundle

from plistlib import readPlist

from objc import Category

import os

from mojo.events import installTool

_images = dict()
def loadImages(imageDir):
    for fileName in os.listdir(imageDir):
        if fileName == ".DS_Store":
            continue
        name, ext = os.path.splitext(fileName)
        if ext in [".png", ".pdf", ".icns"]:
            imagePath = os.path.join(imageDir, fileName)
            _images[name] = NSImage.alloc().initWithContentsOfFile_(imagePath)
            _images[name].setName_(name)

class NSBundle(Category(NSBundle)):
    def resourcePath(self):
        return os.path.join(os.path.dirname(__file__), "dist", "RoboFont.app", "Contents", "Resources")

if __name__ == "__main__":
    print 'RoboFont: initializing'

    loadImages(os.path.join(os.path.dirname(__file__), "Resources", "Images"))
    loadImages(os.path.join(os.path.dirname(__file__), "Resources", "English.lproj"))


    from lib.doodleDocument import DoodleDocument
    from lib.scripting.pyDocument import PyDocument
    from lib.doodleDelegate import DoodleAppDelegate, DoodleApplication

    app = DoodleApplication.sharedApplication()
    delegate = DoodleAppDelegate.alloc().init()
    app.setDelegate_(delegate)

    infoDictPath = os.path.join(os.path.dirname(__file__), "dist", "RoboFont.app", "Contents", "Info.plist")
    defaultInfoDict = readPlist(infoDictPath)

    infoDict = NSBundle.mainBundle().infoDictionary()

    infoDict.update(defaultInfoDict)
    infoDict["CFBundleInfoPlistURL"] = infoDictPath

    nibPath = os.path.join(os.path.dirname(__file__), "Resources", "English.lproj", "MainMenu.nib")
    NSBundle.loadNibFile_externalNameTable_withZone_(nibPath, {}, None)

    app.activateIgnoringOtherApps_(True)

    # Install RoboProject
    # from roboproject.roboprojecttool import RoboProjectTool
    # print 'RoboProject: starting event loop'
    # RoboProjectTool.install()

    # Install RoboProjectFloat
    from roboproject.tools.roboprojecttoolfloat import RoboProjectToolFloat
    print 'RoboProjectFloat: starting event loop'
    RoboProjectToolFloat.install()

    # Install FloqEditor
    from floqeditor.floqeditortool import FloqEditor
    print 'FloqEditor: starting event loop'
    FloqEditor.install()

    AppHelper.runEventLoop()
