#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""dpad.py: Directional pad."""

import math

from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget

__author__ = "Victor RENÉ"
__copyright__ = "Copyright 2014, Kivy widget library"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Victor RENÉ"
__email__ = "victor-rene.dev@outlook.com"
__status__ = "Production"


class Dpad(Widget):

  def __init__(self, **kw):
    super(Dpad, self).__init__(**kw)
    self.listeners = []
    self.thresholds = [(.3, .5), (.7, 1)]
    self.input = [0, 0]
    self.last_touch = None
    with self.canvas.before:
      Color(1, 1, 1, 1)
      self.rect = Rectangle(pos=self.pos, size=self.size, source='img/dpad.png')
    self.bind(pos=self._update_rect)
    self.bind(size=self._update_rect)
    self.polling = kw['polling'] if 'polling' in kw else .01
    Clock.schedule_interval(self.send_input, self.polling)
    
  def _update_rect(self, *args):
    self.rect.pos = self.pos
    self.rect.size = self.size

  def on_touch_down(self, touch):
    self.handle_touch(touch)
    
  def on_touch_move(self, touch):
    self.handle_touch(touch)
    
  def handle_touch(self, touch):
    if self.collide_point(touch.x, touch.y):
      self.last_touch = touch
      dx = (touch.x - self.x - self.width / 2) / self.width * 2
      dy = (touch.y - self.y - self.height / 2) / self.height * 2
      dist = math.sqrt(dx * dx + dy * dy)
      angle = math.atan2(dy, dx)
      self.input = [0, 0]
      for t in self.thresholds:
        if dist > t[0]:
          self.input[0] = t[1] * math.cos(angle)
          self.input[1] = t[1] * math.sin(angle)
      
  def on_touch_up(self, touch):
    if self.last_touch == touch:
      self.input = [0, 0]
      
  def notify(self, event_name, *args, **kw):
    for listener in self.listeners:
      if event_name in listener.handlers:
        getattr(listener, event_name)(*args, **kw)
        
  def send_input(self, dt):
    self.notify('dpad_input', input=self.input)