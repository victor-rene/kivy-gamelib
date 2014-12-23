#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""main.py: Main module."""

from kivy.animation import Animation
from kivy.base import runTouchApp
from kivy.uix.relativelayout import RelativeLayout

from dotmatrix import DotMatrix

__author__ = "Victor RENÉ"
__copyright__ = "Copyright 2014, Kivy widget library"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Victor RENÉ"
__email__ = "victor-rene.dev@outlook.com"
__status__ = "Production"


if __name__ == '__main__':
  layout = RelativeLayout()
  dm_tiny = DotMatrix(size_hint=(.8, .2), pos_hint={'center_x': .5, 'center_y': .7},
    font='font_3x5', dot_style='square', dot_on=(.3,.7,.9,1), dot_off=(0,.1,.3,1))
  dm_tiny.text = '01234 +-.\n56789 =x_'
  layout.add_widget(dm_tiny)
  
  dm_big = DotMatrix(size_hint=(.8, .2), pos_hint={'center_x': .5, 'center_y': .3},
    font='font_5x7')
  dm_big.text = ' ABCDEFGHIJ +-.  0123456789 =x_ '
  layout.add_widget(dm_big)

  # anim = Animation(health=0, duration=2.) + Animation(health=12, duration=2.)
  # anim.repeat = True
  # anim.start(m)
  runTouchApp(layout)
