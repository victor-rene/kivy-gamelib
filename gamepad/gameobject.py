#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""gameobject.py: Just a sprite controlled with the gamepad."""

from kivy.graphics import Color, Ellipse
from kivy.uix.widget import Widget

__author__ = "Victor RENÉ"
__copyright__ = "Copyright 2014, Kivy widget library"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Victor RENÉ"
__email__ = "victor-rene.dev@outlook.com"
__status__ = "Production"


class GameObject(Widget):
  
  def __init__(self, **kw):
    super(GameObject, self).__init__(**kw)
    self.handlers = ['dpad_input', 'bpad_input']
    self.bind(pos=self._update_rect)
    self.bind(size=self._update_rect)
    self.speed = 10
    self.color = (1, 1, 1, 1)
    self.draw()
      
  def _update_rect(self, *args):
    self.draw()
    
  def draw(self):
    self.canvas.clear()
    with self.canvas:
      clr = self.color
      Color(clr[0], clr[1], clr[2], clr[3])
      Ellipse(pos=self.pos, size=self.size)

  def dpad_input(self, *args, **kw):
    dx, dy = kw['input']
    self.x += dx * self.speed
    self.y += dy * self.speed
    
  def bpad_input(self, *args, **kw):
    if kw['btn'] == 'A':
      self.color = (.7, 0, 0, 1)
    elif kw['btn'] == 'B':
      self.color = (.9, .7, 0, 1)
    elif kw['btn'] == 'X':
      self.color = (0, .3, .7, 1)
    elif kw['btn'] == 'Y':
      self.color = (0, .7, 0, 1)
    self.draw()
