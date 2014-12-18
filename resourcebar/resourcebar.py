from kivy.graphics import Color, Quad
from kivy.properties import BoundedNumericProperty
from kivy.uix.widget import Widget


class ResourceBar(Widget):

  fill_pct = BoundedNumericProperty(.5, min=0, max=1)

  def __init__(self, **kw):
    super(ResourceBar, self).__init__(**kw)
    self.slanted = kw['slanted'] if 'slanted' in kw else False
    self.fill_pct = 0.
    self.min_hue = kw['min_hue'] if 'min_hue' in kw else 0
    self.max_hue = kw['max_hue'] if 'max_hue' in kw else 1./3
    with self.canvas.before:
      self.quadbg_color = Color(.1, .4, .4, 1)
      self.quadbg = Quad(source='img/resourcebar_bg.png')
    with self.canvas:
      self.quad_color = Color(.5, .5, .5, 1)
      self.quad = Quad(source='img/resourcebar.png')
    with self.canvas.after:
      self.quadfg_color = Color(.2, .8, .8, 1)
      self.quadfg = Quad(source='img/resourcebar_fg.png')
    self.bind(pos=self._update)
    self.bind(size=self._update)
    self.bind(fill_pct=self._update_fill_pct)
    
  def _update_fill_pct(self, *args):
    """ Set the percentage of the bar between 0 et 1."""
    self._update_quad(self.quad, self.fill_pct)
    self._update_fill_hue(self.fill_pct)
    
  def _update(self, *args):
    self.slant = self.height if self.slanted else 0
    self._update_quad(self.quadbg, 1)
    self._update_quad(self.quad, self.fill_pct)
    self._update_quad(self.quadfg, 1)
    
  def _update_quad(self, quad, pct):
    slant = self.height if self.slanted else 0
    x1 = self.x
    y1 = self.y
    x2 = x1 + self.slant
    y2 = self.y + self.height
    x3 = x2 + self.width * pct
    y3 = y2
    x4 = x1 + self.width * pct
    y4 = y1
    quad.points = [x1, y1, x2, y2, x3, y3, x4, y4]
    
  def _update_fill_hue(self, fill_pct):
    """ Set the percentage of the bar between 0 et 1."""
    h = (self.max_hue - self.min_hue) * fill_pct + self.min_hue
    s = .8
    v = .8
    a = 1
    self.canvas.remove(self.quad_color)
    self.quad_color = Color(h, s, v, a, mode='hsv')
    self.canvas.insert(1, self.quad_color)