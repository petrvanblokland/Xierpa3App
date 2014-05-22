# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#    xierpa server
#    Copyright (c) 2014+  buro@petr.com, www.petr.com, www.xierpa.com
#    
#    X I E R P A  3
#    Distribution by the MIT License.
#
# -----------------------------------------------------------------------------

from xierpa3.server.twistedmatrix.twistedclient import TwistedClient
from xierpa3.sites.doingbydesign.doingbydesign import DoingByDesign
from xierpa3.toolbox.transformer import TX

class SiteDispatcher(object):
    
    def __init__(self):
        self.sites = {
            'ddd': DoingByDesign()
        }

class Client(TwistedClient):

    siteDispatcher = SiteDispatcher()
    doingByDesign = DoingByDesign()
    
    THEMES = {
        # Matching theme names with Theme instances.
        TwistedClient.DEFAULTTHEME: doingByDesign,
    }
   
    def XXXgetSite(self, httprequest):
        return self.siteDispatcher.sites['ddd']
        
    def XXXgetFilePath(self, site):
        u"""
        Answers the file path, based on the URL. Add '/files' to hide Python sources from view.
        The right 2 slash-parts of the site path are taken for the output (@@@ for now)
        """
        site = self.getSite(None)
        return TX.class2Path(site) + '/files/' + '/'.join(site.e.path.split('/')[-2:])
    
