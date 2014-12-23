#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""dotmatrix.py: Displays text and numbers with a matrix of dots."""

import os

from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

from font import Font

__author__ = "Victor RENÉ"
__copyright__ = "Copyright 2014, Kivy widget library"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Victor RENÉ"
__email__ = "victor-rene.dev@outlook.com"
__status__ = "Production"


class DotMatrix(Widget):

  text = StringProperty()

  def __init__(self, **kw):
    super(DotMatrix, self).__init__(**kw)
    self.background = kw['background'] if 'background' in kw \
      else (.1, .1, .1, 1)
    self.dot_on = kw['dot_on'] if 'dot_on' in kw else (.1, .9, .1, 1)
    self.dot_off = kw['dot_off'] if 'dot_off' in kw else (.1, .3, .1, 1)
    self.dot_style = kw['dot_style'] if 'dot_style' in kw else 'circle'
    self.rows = kw['rows'] if 'rows' in kw else 2
    self.cols = kw['cols'] if 'cols' in kw else 16
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    if 'font' in kw:
      self.font = Font(dirname=os.path.join(curr_dir, kw['font']))
    else: self.font = Font(dirname=os.path.join(curr_dir, 'font_5x7'))
    self.spacing = kw['spacing'] if 'spacing' in kw else 1
    self.bind(pos=self.draw)
    self.bind(size=self.draw)
    self.bind(text=self.draw)
    
  def draw(self, *args):
    self.canvas.clear()
    with self.canvas:
      bg = self.background
      Color(bg[0], bg[1], bg[2], bg[3])
      Rectangle(pos=self.pos, size=self.size)
      lines = self.text.split('\n')
      x, y = 0, 0
      for line in reversed(lines):
        for c in line:
          if c in self.font.glyphs:
            glyph = self.font.glyphs[c]
          else: glyph = self.font.glyphs[' ']
          self.draw_glyph(glyph, x, y)
          x += 1
          if x == self.cols:
            x = 0
            y += 1
            continue
        x = 0
        y += 1

  def draw_glyph(self, glyph, x, y):
    row_height = self.height / self.rows
    dot_height = row_height / (self.font.size[1] + 1)
    col_width = self.width / self.cols
    dot_width = col_width / (self.font.size[0] + 1)
    with self.canvas:
      iy = 0
      for row in reversed(glyph.dots):
        ix = 0
        for dot in row:
          if dot:
            Color(self.dot_on[0], self.dot_on[1],
              self.dot_on[2], self.dot_on[3])
          else:
            Color(self.dot_off[0], self.dot_off[1],
              self.dot_off[2], self.dot_off[3])
          x_dot = self.x + x * col_width + ix * dot_width
          y_dot = self.y + y * row_height + iy * dot_height
          if self.dot_style == 'circle':
            Ellipse(pos=(x_dot + dot_width/2., y_dot + dot_height/2.),
              size=(dot_width, dot_height))
          elif self.dot_style == 'square':
            Rectangle(pos=(x_dot + dot_width/2., y_dot + dot_height/2.),
              size=(dot_width, dot_height))
          ix += 1
        iy += 1
