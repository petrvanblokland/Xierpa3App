# -*- coding: UTF-8 -*-
#
#    X I E R P A   3
#    OS X Application (c) 2014 buro@petr.com, www.petr.com, www.xierpa.com.
#    Authors: Petr van Blokland, Michiel Kauw–A–Tjoe.
#
#    No distribution without permission.
#

import vanilla
from constants import Constants

class Xierpa3Window(Constants):
    u"""
    Implementation of a vanilla-based GUI for the Xierpa 3 environment.
    """

    def __init__(self):
        u"""
        Initialize the window and open it.
        """
        self.paths = []
        options = ["Xierpa 3 Server", "HTML + Sass", "Kirby Template", "WordPress Template"]
        self.w = vanilla.Window((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), "Xierpa 3", closable=True)
        self.w.radioGroup = vanilla.RadioGroup((10, 10, -10, 80),
                                options,
                                callback=self.radioGroupCallback)
        self.w.open()

    def radioGroupCallback(self, sender):
        print "radio group edit!", sender.get()

'''
class SpreadsheetDemo(object):

    def __init__(self):
        self.w = Window((400, 400), "Spreadsheet", minSize=(100, 100))
        cols = (
            'Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh',
            'Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh',
            'Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh')
        rows = 5
        self.w.spreadsheet = sh = Spreadsheet((0, 0, 0, 200), cols, rows)
        sh.fill()
        self.w.spreadsheetView = ((100, 0, 0, 0), self.w.spreadsheet.getView())
        self.w.open()

# SpreadsheetDemo()

class StyleFloqSheet(Spreadsheet):
    FIELDS = ('leftMargin', 'width', 'rightMargin', 'stem', 'roundStem', 'bar', 'roundBar')

    def fill(self):
        u"""Initial call or glyph changed: fill the cell data"""
        styleFloq = self.getModel()
        y = 0
        for glyphName in sorted(styleFloq.keys()):
            glyph = styleFloq[glyphName]
            self[(0, y)] = glyphName
            for x, field in enumerate(self.FIELDS):
                value = getattr(styleFloq[glyphName], field) or ''
                self[(x + 1, y)] = value
            y += 1

class StyleFloqSheetDemo(object):
    def __init__(self):
        font = CurrentFont()
        if font is not None:
            self.w = Window((800, 400), "Style Floq Sheet", minSize=(100, 100))
            cols = ('Name', 'Uni', 'Left', 'Width', 'Right', 'Stem', 'rStem', 'Bar', 'rBar')
            rows = len(font.keys())
            styleFloq = floqManager.fromFont(font)
            # print 'rows', rows
            self.w.floqSheet = fs = StyleFloqSheet((0, 0, 0, 0), cols, rows, styleFloq)
            self.w.spreadsheetView = ssv = ScrollView((0, 0, 0, 0), fs.getView())
            fs.setParent(ssv) # Set parent, so the spreadsheet can find the scrollbar value.
            self.w.open()

StyleFloqSheetDemo()
'''