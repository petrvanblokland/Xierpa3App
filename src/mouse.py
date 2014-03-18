# -*- coding: UTF-8 -*-
#
#    X I E R P A   3
#    OS X Application (c) 2014 buro@petr.com, www.petr.com, www.xierpa.com.
#    Authors: Petr van Blokland, Michiel Kauw–A–Tjoe.
#
#    No distribution without permission.
#

class Mouse(object):

    def __init__(self):
        self.p = None
        self.xy = None
        self.dragging = False
        self.modifiers = None

    def __repr__(self):
        return 'Mouse[%s %s %s %s]' % (self.p, self.xy, self.dragging, self.modifiers)
