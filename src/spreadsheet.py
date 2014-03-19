# -*- coding: UTF-8 -*-
#
#    X I E R P A   3
#    OS X Application (c) 2014 buro@petr.com, www.petr.com, www.xierpa.com.
#    Authors: Petr van Blokland, Michiel Kauw–A–Tjoe.
#
#    No distribution without permission.
#
#    Scrolling
#
#    https://developer.apple.com/library/mac/documentation/cocoa/Conceptual/NSScrollViewGuide/Articles/Scrolling.html
#    https://developer.apple.com/library/mac/documentation/cocoa/Conceptual/NSScrollViewGuide/Articles/Scrolling.html#//apple_ref/doc/uid/TP40003463-SW2

import weakref

from AppKit import *
from vanilla import VanillaBaseObject, EditText
# from vanilla import *
from random import random
from mouse import Mouse
from eventview import EventView

class Spreadsheet(VanillaBaseObject):

    # Cell width and height.
    MARGIN = 80
    W = 80
    H = 21
    CELLMARGIN = 4
    TITLEWIDTH = 40
    defaultTextAttributes = {NSFontAttributeName: NSFont.fontWithName_size_("Verdana", 12),
                             NSForegroundColorAttributeName: NSColor.blackColor()}

    def __init__(self, parent, posSize, cols, rows, model=None):
        u"""
        The <b>Spreadsheet</b> defines the generic behavior of a spread sheet. The <i>cols</i> can be an integer,
        indicating the number of columns, or it can be a list of names for all columns. The same applies to the
        <i>rows</i> attribute.
        """
        self._parent = parent
        self._posSize = posSize
        self._cols = range(cols)
        self._rows = range(rows)
        self._width = len(self._cols) * self.W
        self._height = len(self._rows) * self.H
        self._cells = {}
        self._selected = set() # Set (x,y) of selected cells coordinates.

        # Set view.
        self._nsObject = view = EventView.alloc().init()
        view.setFrame_(((0, 0), (self._width, self._height)))
        view.setModel(self)
        self.clearMouse()

        # self._setAutosizingFromPosSize(posSize)

        self.editCell = EditText((0, 0, self.W, self.H), callback=self.editCellCallback)
        self.editCell.show(False)

        self.fill()

    def getParent(self):
        return self._parent

    def setParent(self, parent):
        self._parent = weakref.ref(parent)

    def editCellCallback(self, sender):
        print sender.get()

    def clearMouse(self):
        self._mouse = Mouse()

    def getModel(self):
        # return self._model
        return self

    def getView(self):
        return self._nsObject

    def getWindowSize(self):
        w, h = self._nsObject.bounds()[1]
        return w, h

    def getWindowWidth(self):
        w, _ = self._nsObject.bounds()[1]
        return w

    def getWindowHeight(self):
        _, h = self._nsObject.bounds()[1]
        return h

    def getWindowPosition(self):
        x, y = self._nsObject.bounds()[0]
        return x, y

    #   E V E N T S

    def mouseDown(self, event):
        self._mouse.p = p = event.locationInWindow()
        self._mouse.xy = xy = self.mouse2Cell(p.x, p.y)
        self._mouse.modifiers = modifiers = event.modifierFlags()
        self._mouse.dragging = False

        # Cmd-key, toggle current position
        if modifiers & NSCommandKeyMask:
            self.toggleSelect(xy)
        elif modifiers & NSShiftKeyMask:
            self.marqueeSelect(xy)
        else:
            # Otherwise clear selection and set the current position
            self.clearSelection()
            self.select(xy)
        self.update()

    def mouseUp(self, event):
        u"""
        Shows edit cell with contents.
        """
        if len(self._selected) == 1:
            (ox, oy), (ow, oh) = self.getVisibleScrollRect()
            xy = list(self._selected)[0]
            px, py = self.cell2Mouse(xy)
            self.editCell.set(self[xy])
            # print xy, px, py, self._height - 200
            self.editCell.setPosSize((px, self._height - 200, self.W, self.H))
            self.editCell.show(True)
        else:
            self.editCell.show(False)
        self._mouse.dragging = False
        self.update()

    def mouseDragged(self, event):
        self._mouse.dragging = True
        p = event.locationInWindow()
        xy = self.mouse2Cell(p.x, p.y)
        self.marqueeSelect(xy)
        self.update()

    def keyDown(self, event):
        self._colNames
        print 'keyDown', event

    def keyUp(self, event):
        print 'keyUp', event

    #   S E L E C T I O N

    def clearSelection(self):
        self._selected = set()

    def select(self, xy):
        self._selected.add(xy)

    def toggleSelect(self, xy):
        if xy in self._selected:
            self._selected.remove(xy)
        else:
            self._selected.add(xy)

    def marqueeSelect(self, xy):
        self.clearSelection()
        px, py = xy
        px = int(px)
        py = int(py)
        if self._mouse.xy is not None:
            sx, sy = self._mouse.xy
            sx = int(sx)
            sy = int(sy)
            for x in range(min(px, sx), max(px, sx) + 1):
                for y in range(min(py, sy), max(py, sy) + 1):
                    self.select((x, y))

    #   C O N V E R S I O N

    def mouse2Cell(self, px, py):
        u"""
        Converts point coordinates to discrete cell coordinates. Compensates for clipping frame by adding masked
        pixels to x and masked pixels plus difference between clipping frame height and window height to y.
        """
        (cx, cy), (_, ch) = self.getVisibleScrollRect()

        rx = cx + px # Relative x, clipping x and point x combined.
        ry = py - cy # Relative y, clipping y and point y combined.
        height = self.getWindowHeight()
        cdiff = height - ch + 42 # Compensating 42 for initial difference, should go to initialization.
        ry += cdiff

        x = int(rx / self.W)
        y = int(ry / self.H)
        y = len(self._rows) + 1 - y
        return x, y

    def cell2Mouse(self, x, y=None):
        if y is None:
            x, y = x
        return (x + 1) * self.W, y * self.H

    def getVisibleScrollRect(self):
        u"""
        Get the size of the current scroll rectangle. We only draw there.
        """
        parent = self.getParent()
        return parent.w.scrollView.getNSScrollView().documentVisibleRect()

    #   D A T A

    def __getitem__(self, xy):
        return self._cells.get(xy)

    def __setitem__(self, xy, value):
        self._cells[xy] = value

    def get(self, x, y):
        return self[(x, y)]

    def set(self, x, y, value):
        self[(x, y)] = value

    def keys(self):
        return self._cells.keys()

    def items(self):
        return self._cells.items()

    def rows(self, column):
        u"""
        Answer a list of row cells at column position.
        """
        rows = []
        for y in range(len(self._rows)):
            rows.append(self.get(column, y))
        return rows

    def cols(self, row):
        u"""
        Answer a list of column cells at the row position.
        """
        cols = []
        for x in range(len(self._cols)):
            cols.append(self.get(x, row))
        return cols

    def fill(self):
        u"""
        Initializes cell values.
        """

        i = 0

        for x in range(len(self._cols)):
            for y in range(len(self._rows)):
                # if x == y:
                #    value = '?abc'
                # else:
                #    value = x * y
                value = i
                i += 1
                self.set(x, y, value)

    def evaluate(self, item):
        u"""
        Looks at cell contents to calculate result for each one.
        """
        if isinstance(item, basestring):
            if item.startswith('?'):
                s = '-x-'
            else:
                s = item
        elif isinstance(item, (int, long, float)):
            s = u'%s' % int(round(item))
        else:
            s = u'%s' % item
        return s

    #   D R A W

    def update(self):
        self._nsObject.display()

    def draw(self, rect=None):
        u"""
        Render the cells that fall inside rectangle.
        """
        self.drawGrid(rect)
        # self.drawCells(rect)

    def setLight(self):
        NSColor.colorWithCalibratedRed_green_blue_alpha_(1, 1, 1, 0.5).set()

    def setDark(self):
        NSColor.colorWithCalibratedRed_green_blue_alpha_(0, 0, 0, .1).set()

    def setHighlight(self):
        NSColor.colorWithCalibratedRed_green_blue_alpha_(1, 1, 0, .4).set()

    def drawGrid(self, rect):
        u"""
        Draw the grid lines of the cells and labels of the columns.
        """
        (vy, vx), (vw, vh) = rect
        height = self.getWindowHeight()

        # Draw the horizontal bands of the rows
        for x in self._cols:
            px = x * self.W
            for y in self._rows:
                py = y * self.H
                if y % 2 == 0:
                    self.setLight()
                else:
                    self.setDark()
                box = NSMakeRect(px, py, self.W - 1, self.H - 1)
                path = NSBezierPath.bezierPathWithRect_(box)
                path.fill()
                # str = '%d, %d' % (x, y)
                # self.text(str, px, py)

        # Draw the selected cells as color rectangle
        self.setHighlight()

        for x, y in self._selected:
            py = y * self.H
            px = x * self.W
            box = NSMakeRect(px, py, self.W - 1, self.H - 1)
            path = NSBezierPath.bezierPathWithRect_(box)
            path.fill()

    def drawCells(self, rect):
        u"""
        Draw the evaluated values of the all cells, if they are inside the visible update rectangle.
        """
        (vy, vx), (vw, vh) = rect
        attrs = {NSFontAttributeName : NSFont.fontWithName_size_("Verdana", 12),
                NSForegroundColorAttributeName : NSColor.blackColor()
        }

        for (x, y), item in self.items():
            # print x, y, vx, vy, vw, vh, item
            px, py = self.cell2Mouse(x, y)
            if vy <= py < vy + vh:
                self.text(self.evaluate(item), px, py, attrs)

    def text(self, txt, x, y, attrs=None, align='right'):
        u"""
        Draw the text in cell position x, y.
        """

        if not isinstance(txt, basestring):
            txt = `txt`

        attrs = attrs or self.defaultTextAttributes
        # if align == 'right':
        #    w = self.getStringWidth(txt, attrs)
        #    offset = self.MARGIN - w - self.CELLMARGIN
        # else:
        offset = self.CELLMARGIN
        text = NSAttributedString.alloc().initWithString_attributes_(txt, attrs)

        try:
            text.drawAtPoint_((x + offset, y))
        except Exception, e:
            print e

    def getStringWidth(self, txt, attrs):
        s = NSString.stringWithString_(txt)
        r = s.boundingRectWithSize_options_attributes_((0, 0), 1, attrs)
        return r.size.width
