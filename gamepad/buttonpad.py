#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""gameobject.py: Just a sprite controlled with the gamepad."""

from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

__author__ = "Victor RENÉ"
__copyright__ = "Copyright 2014, Kivy widget library"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Victor RENÉ"
__email__ = "victor-rene.dev@outlook.com"
__status__ = "Production"


class ButtonPad(Widget):

  def __init__(self, **kw):
    super(ButtonPad, self).__init__(**kw)
    self.listeners = []
    self.layout = RelativeLayout()
    self.add_widget(self.layout)
    btn_ids = ['A', 'B', 'X', 'Y']
    btn_pos = [(.8, .5), (.5, .2), (.5, .8), (.2, .5)]
    btn_colors = [[.7,0,0,1],[.9,.7,0,1],[0,.3,.7,1],[0,.7,0,1]]
    for i in range(4):
      btn = Button(id=btn_ids[i], size_hint=(.2, .2),
        background_color=btn_colors[i],
        background_normal='img/btn-normal.png',
        background_down='img/btn-down.png',
        pos_hint={'center_x': btn_pos[i][0], 'center_y': btn_pos[i][1]})
      btn.bind(on_press=self.btn_press)
      self.layout.add_widget(btn)
    with self.canvas.before:
      Color(1, 1, 1, 1)
      self.rect = Rectangle(pos=self.pos, size=self.size, source='img/bpad.png')
    self.bind(pos=self._update_rect)
    self.bind(size=self._update_rect)
    # self.polling = kw['polling'] if 'polling' in kw else .01
    # Clock.schedule_interval(self.send_input, self.polling)
    
  def _update_rect(self, *args):
    self.rect.pos = self.pos
    self.rect.size = self.size
    self.layout.pos = self.pos
    self.layout.size = self.size
    
  def btn_press(self, btn):
    self.notify('bpad_input', btn=btn.id)
      
  def notify(self, event_name, *args, **kw):
    for listener in self.listeners:
      if event_name in listener.handlers:
        getattr(listener, event_name)(*args, **kw)
        
  # def send_input(self, dt):
    # self.notify('bpad_input', input=self.input)