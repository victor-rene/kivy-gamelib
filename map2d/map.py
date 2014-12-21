from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ListProperty, StringProperty


class Map2D(RelativeLayout):

  player_icon = StringProperty()
  player_pos = ListProperty()

  def __init__(self, **kw):
    super(Map2D, self).__init__(**kw)
    self.map_size = kw['map_size'] if 'map_size' in kw else (3, 3)
    self.room_size = (1./self.map_size[0], 1./self.map_size[1])
    self.rooms = dict()
    self.center_room = None # TODO set coords to offset drawing of rooms
    
  def draw_rooms(self):
    self.clear_widgets()
    for k, v in self.rooms.iteritems():
      x = k[0] * self.room_size[0]
      y = k[1] * self.room_size[1]
      v.pos_hint = {'x': x, 'y': y}
      v.size_hint = self.room_size
      self.add_widget(v)
      v.draw()
