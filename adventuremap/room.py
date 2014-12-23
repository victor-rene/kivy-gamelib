from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, OptionProperty, StringProperty


class Room(Widget):

  def __init__(self, **kw):
    super(Room, self).__init__(**kw)
    self.background = kw['background'] if 'background' in kw else (0, .5, 1, 1)
    self.doors = kw['doors'] if 'doors' in kw else [None for i in range(4)]
    self.walls = kw['walls'] if 'walls' in kw else ['full' for i in range(4)]
    self.state = kw['state'] if 'state' in kw else 'hidden'
    self.powerup = None
    self.bind(pos=self.draw)
    self.bind(size=self.draw)
    
  def get_points(self):
    x1, y1 = self.x+2, self.y+2
    x2, y2 = self.x+2, self.y-3 + self.height
    x3, y3 = self.x-3 + self.width, y2
    x4, y4 = x3, y1
    return [x1, y1, x2, y2, x3, y3, x4, y4]
    
  def draw(self, *args):
    self.canvas.clear()
    self.draw_background()
    self.draw_walls()
    self.draw_doors()
    self.draw_powerup()

  def draw_background(self):
    with self.canvas:
      if self.state == 'hidden':
        Color(.1, .1, .1, 1)
        Rectangle(pos=self.pos, size=self.size)
      elif self.state == 'revealed':
        Color(.5, .5, .5, 1)
        Rectangle(pos=self.pos, size=self.size)
      else: # explored
        bg = self.background
        Color(bg[0], bg[1], bg[2], bg[3])
        Rectangle(pos=self.pos, size=self.size)
  
  def draw_walls(self):
    points = self.get_points()
    with self.canvas:
      for i in range(4):
        wall = self.walls[i]
        if self.state == 'hidden':
          Color(0, .2, 0, 1)
          x1, y1 = points[i * 2], points[i * 2 + 1]
          x2, y2 = points[(i * 2 + 2)  % 8], points[(i * 2 + 3) % 8]
          Line(points=[x1, y1, x2, y2], width=2)
        else:
          if wall == 'full':
            Color(1, 1, 1, 1)
            x1, y1 = points[i * 2], points[i * 2 + 1]
            x2, y2 = points[(i * 2 + 2)  % 8], points[(i * 2 + 3) % 8]
            Line(points=[x1, y1, x2, y2], width=2)
          elif wall == 'gap':
            Line()
            Line()
  
  def draw_doors(self):
    for door in self.doors:
      Color()
      Rectangle()
      Color(1, 1, 1, 1)
      Line()
      Line()
  
  def draw_powerup(self):
    if self.powerup == 'on':
      with self.canvas:
        Ellipse()
    elif self.powerup == 'off':
      with self.canvas:
        pass
        # Line(ellipse=None)
