#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""font.py: Represents a font for a dot matrix."""

import os

from glyph import Glyph

__author__ = "Victor RENÉ"
__copyright__ = "Copyright 2014, Kivy widget library"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Victor RENÉ"
__email__ = "victor-rene.dev@outlook.com"
__status__ = "Production"


class Font(object):

  def __init__(self, **kw):
    self.glyphs = dict()
    self.size = 0, 0
    if 'dirname' in kw:
      self.read(kw['dirname'])
    
  def read(self, dirname):
    files = os.listdir(dirname)
    for file in files:
      name = file[-5:-4]
      print name
      curr_dir = os.path.dirname(os.path.realpath(__file__))
      self.glyphs[name] = Glyph(filename=os.path.join(curr_dir, dirname, file))
      w = self.glyphs[name].size[0]
      h = self.glyphs[name].size[1]
      self.size = max(self.size[0], w), max(self.size[1], h)