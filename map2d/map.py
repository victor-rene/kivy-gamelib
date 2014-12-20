from kivy.uix.widget import Widget


class Map(Widget):

  player_icon = StringProperty()
  player_pos = ListProperty()

  def __init__(self, **kw)
    super(Map, self).__init__(**kw)
    self.map_size = kw['map_size'] if map_size in kw else (3, 3)
