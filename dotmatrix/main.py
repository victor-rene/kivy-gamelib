#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""main.py: Main module."""

from functools import partial

from kivy.clock import Clock
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


def rotate_text(wgt, dt):
  wgt.text = wgt.text[1:] + wgt.text[:1]

if __name__ == '__main__':
  layout = RelativeLayout()
  dm_tiny = DotMatrix(size_hint=(.8, .2), pos_hint={'center_x': .5, 'center_y': .7},
    font='font_3x5', dot_style='square', dot_on=(.3,.7,.9,1), dot_off=(0,.1,.3,1))
  dm_tiny.text = ' ABCDEFGHIJ +-.  0123456789 =*/ '
  layout.add_widget(dm_tiny)
  
  dm_big = DotMatrix(size_hint=(.8, .2), pos_hint={'center_x': .5, 'center_y': .3},
    font='font_5x7')
  dm_big.text = ' ABCDEFGHIJ +-.  0123456789 =*/ '
  layout.add_widget(dm_big)

  Clock.schedule_interval(partial(rotate_text, dm_big), 1)
  runTouchApp(layout)
