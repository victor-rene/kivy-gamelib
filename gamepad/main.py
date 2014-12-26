#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""main.py: Main module."""

from kivy.base import runTouchApp
from kivy.uix.relativelayout import RelativeLayout

from dpad import Dpad
from buttonpad import ButtonPad
from gameobject import GameObject

__author__ = "Victor RENÉ"
__copyright__ = "Copyright 2014, Kivy widget library"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Victor RENÉ"
__email__ = "victor-rene.dev@outlook.com"
__status__ = "Production"


if __name__ == '__main__':
  layout = RelativeLayout()
  d = Dpad(size_hint=(.15, .2), pos_hint={'center_x': .1, 'center_y': .5})
  layout.add_widget(d)
  b = ButtonPad(size_hint=(.15, .2), pos_hint={'center_x': .9, 'center_y': .5})
  layout.add_widget(b)
  go = GameObject(size_hint=(.075, .1), pos_hint={'center_x': .5, 'center_y': .5})
  d.listeners.append(go)
  b.listeners.append(go)
  layout.add_widget(go)
  runTouchApp(layout)
