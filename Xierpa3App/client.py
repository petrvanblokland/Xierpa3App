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
from xierpa3.descriptors.environment import Environment

class Client(TwistedClient):

    def getDoIndent(self):
        u"""Answer the boolean flag (UI option in the application) to build with or without indent."""
        return self.app.getDoIndent()

    def getSite(self, httprequest):
        site = self.app.getSite()
        site.e = Environment(request=httprequest)
        # Callback to application, to allow showing request, handle form stuff, etc.
        self.app.handleRequest(httprequest, site)
        return site
