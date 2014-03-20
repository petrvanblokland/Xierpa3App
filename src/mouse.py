# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#    RoboFlight
#    (c) 2010 buro@petr.com, www.petr.com
#
#    R O B O F L I G H T
#    No distribution without permission.
#
# -----------------------------------------------------------------------------
#
#    mouse.py
#

class Mouse(object):

    def __init__(self):
        self.p = None
        self.xy = None
        self.dragging = False
        self.modifiers = None

    def __repr__(self):
        return 'Mouse[%s %s %s %s]' % (self.p, self.xy, self.dragging, self.modifiers)
