from kivy.animation import Animation
from kivy.base import runTouchApp
from kivy.uix.relativelayout import RelativeLayout

from heartbar import HeartBar


if __name__ == '__main__':
  layout = RelativeLayout()
  hb = HeartBar(size_hint=(.6, .2), pos_hint={'center_x': .45, 'center_y': .5})
  layout.add_widget(hb)
  anim = Animation(health=0, duration=2.) + Animation(health=12, duration=2.)
  anim.repeat = True
  anim.start(hb)
  runTouchApp(layout)
