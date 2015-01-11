from kivy.animation import Animation
from kivy.base import runTouchApp
from kivy.uix.relativelayout import RelativeLayout

from resourcebar import ResourceBar


if __name__ == '__main__':
  layout = RelativeLayout()
  rb = ResourceBar(size_hint=(.6, .2),
    pos_hint={'center_x': .5, 'center_y': .5})
  layout.add_widget(rb)
  anim1 = Animation(fill_pct=1.) + Animation(fill_pct=0.)
  anim1.repeat = True
  anim1.start(rb)
  anim2 = Animation(slant_pct=-1.) + Animation(slant_pct=1.)
  anim2.repeat = True
  anim2.start(rb)
  runTouchApp(layout)
