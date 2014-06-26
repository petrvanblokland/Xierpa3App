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
import webbrowser
from constants import AppC
from vanilla import RadioGroup, Window, Button, CheckBox, EditText, TextEditor
from xierpa3.sites.doingbydesign.doingbydesign import DoingByDesign
from xierpa3.builders.cssbuilder import CssBuilder
#from xierpa3.builders.htmlbuilder import HtmlBuilder 
from xierpa3.builders.phpbuilder import PhpBuilder
from xierpa3.adapters import PhpAdapter
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
        self.w = Window((AppC.WINDOW_WIDTH, AppC.WINDOW_HEIGHT), "Xierpa 3",
            closable=True, minSize=(200, 200), maxSize=(1600, 1000))
        siteLabels = self.getSiteLabels()
        y = len(siteLabels)*20
        self.w.optionalSites = RadioGroup((10, 10, 150, y), siteLabels,
            callback=self.selectSiteCallback, sizeStyle='small')
        self.w.optionalSites.set(0)
        self.w.openSite = Button((10, y+20, 150, 20), 'Open site', callback=self.openSiteCallback, sizeStyle='small')
        self.w.openCss = Button((10, y+45, 150, 20), 'Open CSS', callback=self.openCssCallback, sizeStyle='small')
        self.w.openSass = Button((10, y+70, 150, 20), 'Open SASS', callback=self.openSassCallback, sizeStyle='small')
        self.w.openDocumentation = Button((10, y+95, 150, 20), 'Documentation', callback=self.openDocumentationCallback, sizeStyle='small')
        self.w.openAsPhp = Button((10, y+120, 150, 20), 'Open as PHP', callback=self.openAsPhpCallback, sizeStyle='small')
        self.w.openAsPhp.enable(False) # For now.
        #self.w.makeSite = Button((10, y+95, 150, 20), 'Make site', callback=self.makeSiteCallback, sizeStyle='small')
        self.w.forceCss = CheckBox((180, 10, 150, 20), 'Force make CSS', sizeStyle='small')
        self.w.doIndent = CheckBox((180, 30, 150, 20), 'Build indents', sizeStyle='small', value=True)
        self.w.console = EditText((10, -200, -10, -10), sizeStyle='small')
        self.w.script = TextEditor((300, 10, -10, -240))
        self.w.runScript = Button((300, -230, 150, -210), 'Run script', 
            callback=self.runScriptCallback, sizeStyle='small')
        self.w.script.set(self.EXAMPLE_SCRIPT)
        self.w.open()

    def getSiteLabels(self):
        siteLabels = []
        for siteLabel, _ in self.SITE_LABELS:
            siteLabels.append(siteLabel)
        return siteLabels

    def runScriptCallback(self, sender):
        src = self.BASESCRIPT + self.w.script.get()
        cc = compile(src, 'abc', mode='exec')
        eval(cc, {'currentSite': self.getSite()})
        #, self.getSite().__dict__)

    def selectSiteCallback(self, sender):
        pass

    def openSiteCallback(self, sender):
        self.openSiteInBrowser(self.URL)

    def openSiteInBrowser(self, url):
        if self.w.forceCss.get():
            url += '/' + C.PARAM_FORCE
        webbrowser.open(url)
    
    def openCssCallback(self, sender):
        url = self.URL
        if self.w.forceCss.get():
            url += '/' + C.PARAM_FORCE
        webbrowser.open(url + '/css/style.css')

    def openSassCallback(self, sender):
        url = self.URL
        #os.open(url + '/css/style.scss')

    def openDocumentationCallback(self, sender):
        url = self.URL
        webbrowser.open(url + '/' + C.PARAM_DOCUMENTATION + '/' + C.PARAM_FORCE)

    def openAsPhpCallback(self, sender):
        u"""Save site as PHP template in MAMP area and then open it in the browser.
        This function assumes that a PHP server like MAMP is running. Otherwise the
        page will not open in the browser."""
        # TODO: Root of the MAMP file. Should become a config variable.
        ROOT_MAMP = '/Applications/MAMP/htdocs/'
        # Get the current selected site instance.
        site = self.getSite()
        saveAdapter = site.adapter # Save the current adapter for this site.
        site.adapter = PhpAdapter() # Create the site running with this adapter.
        rootPath = ROOT_MAMP + site.__class__.__name__.lower() + '/' # TODO: Ask for save folder instead
        # Create the main blog builder, which will split into building the
        # CSS and PHP/HTML files, using the Kirby PHP snippets as content.
        cssBuilder = CssBuilder()
        site.build(cssBuilder) # Build from entire site theme, not just from template. Result is stream in builder.
        cssBuilder.save(site, root=rootPath)
        # Build the PHP/HTML template.
        phpBuilder = PhpBuilder()
        # Make the PHP source directly save to MAMP, so it is served by local server.
        # Build the CSS and and PHP/HTML files in the MAMP directory.
        site.build(phpBuilder) # Build from entire site theme, not just from template. Result is stream in builder.
        phpBuilder.save(site, root=rootPath)
        # Restore the original adapter.
        site.adapter = saveAdapter
           
    def getSite(self):
        _, site = self.SITE_LABELS[self.w.optionalSites.get()]
        return site

    def makeSiteCallback(self, sender):
        self.getSite().make()

    def handleRequest(self, httprequest, site):
        self.addConsole(`httprequest` + ' ' + `site.e.form`)

    def addConsole(self, s):
        self.w.console.set(self.w.console.get() + '\n' + s)

    def getDoIndent(self):
        u"""Answer true if building output code with indent."""
        return self.w.doIndent.get()

