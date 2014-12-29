from functools import partial

from kivy.app import runTouchApp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout

from bone import Bone
from stickman import StickMan

Window.size = 1280, 800

if __name__ == '__main__':
  layout = RelativeLayout()
  sm = StickMan(pos_hint={'center_x': .5, 'center_y': .5},
    size_hint=(10/16.,1))
  layout.add_widget(sm)
  sm.flex()
  runTouchApp(layout)
