from kivy.animation import Animation
from kivy.base import runTouchApp
from kivy.uix.relativelayout import RelativeLayout

from map import Map2D
from room import Room


if __name__ == '__main__':
  layout = RelativeLayout()
  m = Map2D(size_hint=(1, 1), pos_hint={'center_x': .5, 'center_y': .5})
  m.rooms[(0, 0)] = Room()
  m.rooms[(1, 1)] = Room(state='explored', walls=[None, 'full', None, 'full'])
  m.rooms[(1, 0)] = Room()
  m.rooms[(0, 1)] = Room(state='revealed', walls=['full', 'full', None, 'full'])
  m.rooms[(0, 2)] = Room()
  m.rooms[(2, 0)] = Room()
  m.rooms[(2, 2)] = Room()
  m.rooms[(1, 2)] = Room()
  m.rooms[(2, 1)] = Room()
  layout.add_widget(m)
  m.draw_rooms()

  # anim = Animation(health=0, duration=2.) + Animation(health=12, duration=2.)
  # anim.repeat = True
  # anim.start(m)
  runTouchApp(layout)
