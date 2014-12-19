from kivy.properties import NumericProperty
from kivy.uix.image import Image
from kivy.uix.stacklayout2 import StackLayout


class HeartBar(StackLayout):

  health = NumericProperty(0)
  max_health = NumericProperty(12)

  def __init__(self, **kw):
    super(HeartBar, self).__init__(**kw)
    self.orientation = 'tb-lr'
    self.hitpoints = []
    self.bind(health=self.set_health)
    
  def set_health(self, *args):
    """ Each heart is worth 4 pts. """
    del self.hitpoints[:]
    value = self.health
    for i in range(self.max_health / 4):
      if value > 4:
        n = 4
      elif value <= 0:
        n = 0
      else: n = int(value)
      self.hitpoints.append(n)
      value -= 4
    self._draw_health()
      
  def _draw_health(self):
    self.clear_widgets()
    i = 0
    while i < (self.max_health / 4):
      heart = Image(size=(80, 80))
      heart.source = 'img/heart-' + str(self.hitpoints[i]) + '.png'
      self.add_widget(heart)
      i += 1