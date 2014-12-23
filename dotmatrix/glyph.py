#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""glyph.py: Represents a glyph for a dot matrix."""

__author__ = "Victor RENÉ"
__copyright__ = "Copyright 2014, Kivy widget library"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Victor RENÉ"
__email__ = "victor-rene.dev@outlook.com"
__status__ = "Production"


class Glyph(object):

  def __init__(self, **kw):
    if 'filename' in kw:
      self.size = self.get_size(kw['filename'])
      self.dots = [[None for x in range(self.size[0])] for y in range(self.size[1])]
      self.read(kw['filename'])
      
  def get_size(self, filename):
    x_max, y_max = 0, 0
    with open(filename, 'r') as f:
      x, y = 0, 0
      for line in f:
        line = line.strip('\n')
        for dot in line:
          x += 1
          x_max = max(x_max, x)
        x = 0
        y += 1
        y_max = max(y_max, y)
    return x_max, y_max
    
  def read(self, filename):
    with open(filename, 'r') as f:
      x, y = 0, 0
      for line in f:
        line = line.strip('\n')
        for dot in line:
          if dot == ' ':
            self.dots[y][x] = False
          else:
            self.dots[y][x] = True
          x += 1
        x = 0
        y += 1
  
  def write(self, filename):
    pass