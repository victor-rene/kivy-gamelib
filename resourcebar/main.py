from kivy.animation import Animation
from kivy.base import runTouchApp
from kivy.uix.relativelayout import RelativeLayout

from resourcebar import ResourceBar


if __name__ == '__main__':
  layout = RelativeLayout()
  rb = ResourceBar(slanted=True, size_hint=(.6, .2),
    pos_hint={'center_x': .45, 'center_y': .5})
  layout.add_widget(rb)
  anim = Animation(fill_pct=1) + Animation(fill_pct=0)
  anim.repeat = True
  anim.start(rb)
  runTouchApp(layout)
