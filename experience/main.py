from kivy.app import runTouchApp
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

import xp

class Grinder(BoxLayout):
  xp = NumericProperty()
  level = NumericProperty()
  def __init__(self, **kw):
    super(Grinder, self).__init__(**kw)
    self.ids['xp'] = Label(id='xp', size_hint=(1, 1))
    self.add_widget(self.ids['xp'])
    self.ids['lvl'] = Label(id='lvl', size_hint=(1, 1))
    self.add_widget(self.ids['lvl'])
    self.bind(xp=self.update_xp, level=self.update_level)
  def update_xp(self, *args):
    self.ids['xp'].text = str(self.xp)
  def update_level(self, *args):
    self.ids['lvl'].text = str(self.level)
  
def update_xp(dt):
  xp.inc_xp(grinder, 10)
  if grinder.level == grinder.level_max:
    return False

if __name__ == "__main__":
  grinder = Grinder()
  xp.init_xp(grinder)
  Clock.schedule_interval(update_xp, .1)
  runTouchApp(grinder)