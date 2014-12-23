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
      curr_dir = os.path.dirname(os.path.realpath(__file__))
      filename = os.path.join(curr_dir, dirname, file)
      with open(filename) as f:
        text = f.read()
        d = eval(text)
        for k, v in d.iteritems():
          self.glyphs[k] = Glyph(data=v.split('\n')[1:-1])
          w = self.glyphs[k].size[0]
          h = self.glyphs[k].size[1]
          self.size = max(self.size[0], w), max(self.size[1], h)