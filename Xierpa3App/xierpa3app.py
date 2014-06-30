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
import os
import webbrowser
from AppKit import NSInformationalAlertStyle #@UnresolvedImport
from constants import AppC
from vanilla import RadioGroup, Window, Button, CheckBox, EditText, TextEditor, TextBox
from vanilla.dialogs import message
from xierpa3.sites.doingbydesign.doingbydesign import DoingByDesign
from xierpa3.builders.sassbuilder import SassBuilder
from xierpa3.builders.cssbuilder import CssBuilder
from xierpa3.builders.htmlbuilder import HtmlBuilder 
from xierpa3.builders import PhpBuilder
#from xierpa3.adapters import PhpAdapter
#from xierpa3.adapters.kirby.kirbyadapter import KirbyAdapter
from xierpa3.constants.constants import C
from xierpa3.sites.examples import HelloWorld, HelloWorldLayout, HelloWorldBluePrint, \
    HelloWorldResponsive, OneColumnSite, SimpleTypeSpecimenSite, SimpleWebSite, \
    SimpleResponsivePage, Featuring1 

class Xierpa3App(AppC):
    u"""Implementation of a vanilla-based GUI for the Xierpa 3 environment."""

    PORT = 8060
    URL = 'http://localhost:%d' % PORT

    EXAMPLE_SCRIPT = """
s = CurrentSite()
page = s.components[0]
print page
print page.name
"""
    SITE_LABELS = [
        ("Hello world", HelloWorld()),
        ("Hello world layout", HelloWorldLayout()),
        ("Hello world BluePrint", HelloWorldBluePrint()),
        ("Hello world responsive", HelloWorldResponsive()),
        ("Simple responsive page", SimpleResponsivePage()),
        ("One column", OneColumnSite()),
        ("Simple type specimen", SimpleTypeSpecimenSite()),
        ("Simple website", SimpleWebSite()),
        ("Featured article 1", Featuring1()),
        ("DoingByDesign", DoingByDesign()),
    ]
    def __init__(self):
        u"""
        Initialize the window and open it.
        """
        self.w = view = Window((AppC.WINDOW_WIDTH, AppC.WINDOW_HEIGHT), "Xierpa 3",
            closable=True, minSize=(200, 200), maxSize=(1600, 1000))
        siteLabels = self.getSiteLabels()
        y = len(siteLabels)*20
        bo = 25 # Button offset
        view.optionalSites = RadioGroup((10, 10, 150, y), siteLabels,
            callback=self.selectSiteCallback, sizeStyle='small')
        self.w.optionalSites.set(0)
        y = y + 20
        view.openSite = Button((10, y, 150, 20), 'Open site', callback=self.openSiteCallback, sizeStyle='small')
        y += bo
        self.w.saveSite = Button((10, y, 150, 20), 'Save HTML+CSS', callback=self.saveSiteCallback, sizeStyle='small')
        y += bo
        view.openCss = Button((10, y, 150, 20), 'Open CSS', callback=self.openCssCallback, sizeStyle='small')
        y += bo
        view.openSass = Button((10, y, 150, 20), 'Open SASS', callback=self.openSassCallback, sizeStyle='small')
        y += bo
        view.openDocumentation = Button((10, y, 150, 20), 'Documentation', callback=self.openDocumentationCallback, sizeStyle='small')
        y += bo
        view.openAsPhp = Button((10, y, 150, 20), 'Open as PHP', callback=self.openAsPhpCallback, sizeStyle='small')
        #view.makeSite = Button((10, y+95, 150, 20), 'Make site', callback=self.makeSiteCallback, sizeStyle='small')
        view.forceCss = CheckBox((180, 10, 150, 20), 'Force make CSS', sizeStyle='small')
        view.doIndent = CheckBox((180, 30, 150, 20), 'Build indents', sizeStyle='small', value=True)
        view.console = EditText((10, -200, -10, -10), sizeStyle='small')
        # Path defaults
        y = 20
        view.mampRootLabel = TextBox((300, y, 100, 20), 'MAMP folder', sizeStyle='small')
        view.mampRoot = EditText((400, y, -10, 20), C.PATH_MAMP, sizeStyle='small')
        y += bo
        view.exampleRootLabel = TextBox((300, y, 100, 20), 'Root folder', sizeStyle='small')
        view.exampleRoot = EditText((400, y, -10, 20), C.PATH_EXAMPLES, sizeStyle='small') 
        # Scripting
        y += bo
        view.script = TextEditor((300, y, -10, -240))
        view.runScript = Button((500, -230, 150, -210), 'Run script', 
            callback=self.runScriptCallback, sizeStyle='small')
        view.script.set(self.EXAMPLE_SCRIPT)
        view.open()

    def getView(self):
        return self.w
        
    def getSiteLabels(self):
        siteLabels = []
        for siteLabel, _ in self.SITE_LABELS:
            siteLabels.append(siteLabel)
        return siteLabels

    def runScriptCallback(self, sender):
        view = self.getView()
        src = self.BASESCRIPT + view.script.get()
        cc = compile(src, 'abc', mode='exec')
        eval(cc, {'currentSite': self.getSite()})
        #, self.getSite().__dict__)

    def selectSiteCallback(self, sender):
        pass

    def openSiteCallback(self, sender):
        self.openSiteInBrowser(self.URL)

    def updateBuilderRootPaths(self):
        view = self.getView()
        rootPath = view.exampleRoot.get()
        HtmlBuilder.ROOT_PATH = rootPath
        SassBuilder.ROOT_PATH = rootPath
        CssBuilder.ROOT_PATH = rootPath
        
    def saveSiteCallback(self, sender):
        self.updateBuilderRootPaths()
        site = self.getSite()
        site.make()
        path = self.getExampleRootPath(site)
        if path is not None:
            webbrowser.open('file:' + path)
        
    def openSiteInBrowser(self, url):
        self.updateBuilderRootPaths()
        view = self.getView()
        if view.forceCss.get():
            url += '/' + C.PARAM_FORCE
        webbrowser.open(url)
    
    def openCssCallback(self, sender):
        view = self.getView()
        self.updateBuilderRootPaths()
        url = self.URL
        if view.forceCss.get():
            url += '/' + C.PARAM_FORCE
        webbrowser.open(url + '/css/style.css')

    def openSassCallback(self, sender):
        url = self.URL
        #os.open(url + '/css/style.scss')

    def openDocumentationCallback(self, sender):
        self.updateRootPaths()
        url = self.URL
        webbrowser.open(url + '/' + C.PARAM_DOCUMENTATION + '/' + C.PARAM_FORCE)

    def getMampRootPath(self, site):
        view = self.getView()
        root = os.path.expanduser(view.mampRoot.get()) # File root of server.
        if not root.endswith('/'):
            root += '/'
        if not os.path.exists(root):
            message(messageText='Error in MAMP path.', informativeText='The MAMP folder "%s" does not exist.' % root, 
                alertStyle=NSInformationalAlertStyle, parentWindow=view)
            return None
        return root + site.__class__.__name__.lower() + '/' 
    
    def getExampleRootPath(self, site):
        view = self.getView()
        root = os.path.expanduser(view.exampleRoot.get()) # File root of server.
        if not root.endswith('/'):
            root += '/'
        if not os.path.exists(root):
            message(messageText='Error in Examples path.', informativeText='The Examples folder "%s" does not exist.' % root, 
                alertStyle=NSInformationalAlertStyle, parentWindow=view)
            return None
        return root + site.__class__.__name__.lower() + '/' 
        
    def openAsPhpCallback(self, sender):
        u"""Save site as PHP template in MAMP area and then open it in the browser.
        This function assumes that a PHP server like MAMP is running. Otherwise the
        page will not open in the browser."""
        # Get the current selected site instance.
        site = self.getSite()
        # Save the current adapter for this site in order to restore it in the end.
        # The site instance is create on startup, and we don't want to destroy
        # the original default adapter that is already there.
        saveAdapter = site.adapter 
        #site.adapter = PhpAdapter() # Create the site running with this adapter.
        rootPath = self.getMampRootPath(site)
        # Build the CSS and and PHP/HTML files in the MAMP directory.
        builder = CssBuilder()
        site.build(builder) # Build from entire site theme, not just from template. Result is stream in builder.
        builder.save(site, root=rootPath)
        # Create the PhpBuilder instance that can build/modify the PHP file structure.
        builder = PhpBuilder()
        # Render the website towards PHP export.
        site.build(builder) # Build from entire site theme, not just from template. Result is stream in builder.
        # Copy the PHP frame work and save PHP/HTML files,
        builder.save(site, root=rootPath)
        # Restore the original adapter.
        site.adapter = saveAdapter
           
    def getSite(self):
        view = self.getView()
        _, site = self.SITE_LABELS[view.optionalSites.get()]
        return site

    def makeSiteCallback(self, sender):
        self.getSite().make()

    def handleRequest(self, httprequest, site):
        self.addConsole(`httprequest` + ' ' + `site.e.form`)

    def addConsole(self, s):
        view = self.getView()
        view.console.set(view.console.get() + '\n' + s)

    def getDoIndent(self):
        u"""Answer true if building output code with indent."""
        view = self.getView()
        return view.doIndent.get()

