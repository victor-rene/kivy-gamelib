from kivy.graphics import Color, Quad
from kivy.properties import BoundedNumericProperty, NumericProperty
from kivy.uix.widget import Widget


class ResourceBar(Widget):

  slant_pct = BoundedNumericProperty(.0, min=-1., max=1.)
  fill_pct = BoundedNumericProperty(.0, min=0., max=1.)
  min_hue = BoundedNumericProperty(.0, min=0., max=1.)
  max_hue = BoundedNumericProperty(1./3, min=0., max=1.)
  padding_x = NumericProperty(5.)
  padding_y = NumericProperty(0.)

  def __init__(self, **kw):
    super(ResourceBar, self).__init__(**kw)
    for k, v in kw.iteritems():
        if hasattr(self, k):
            setattr(self, k, v)
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
    self.bind(slant_pct=self._update_slant_pct)
    
  def _update_fill_pct(self, *args):
    """ Set the fill percentage of the bar (between 0 et 1). """
    self._update_quad(self.quad, self.fill_pct)
    self._update_fill_hue(self.fill_pct)
    
  def _update_slant_pct(self, *args):
    """ Set the fill percentage of the bar (between 0 et 1). """
    self._update_quad(self.quadbg, 1.)
    self._update_quad(self.quadfg, 1.)
    
  def _update(self, *args):
    """ Update all quads. """
    self._update_quad(self.quadbg, 1)
    self._update_quad(self.quad, self.fill_pct)
    self._update_quad(self.quadfg, 1)
    
  def _update_quad(self, quad, pct):
    """ Update one qued. """
    padding_x = self.padding_x if quad == self.quad else 0.
    padding_y = self.padding_y if quad == self.quad else 0.
    x1 = self.x + padding_x
    y1 = self.y + padding_y
    x2 = x1 + (self.height * self.slant_pct) + padding_x
    y2 = self.y + self.height - (padding_y * 2)
    x3 = x2 + (self.width * pct) - (padding_x * 2)
    y3 = y2
    x4 = x1 + (self.width * pct) - (padding_x * 2)
    y4 = y1
    quad.points = [x1, y1, x2, y2, x3, y3, x4, y4]
    
  def _update_fill_hue(self, fill_pct):
    """ Set the color of the bar. """
    h = (self.max_hue - self.min_hue) * fill_pct + self.min_hue
    s = .8
    v = .8
    a = 1
    self.canvas.remove(self.quad_color)
    self.quad_color = Color(h, s, v, a, mode='hsv')
    self.canvas.insert(1, self.quad_color)