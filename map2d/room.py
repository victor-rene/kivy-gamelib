from kivy.uix.widget import Widget


class Room(Widget):

  background = ListProperty()
  state = StringProperty()
  walls = ListProperty()
  doors = ListProperty()
  powerup = OptionProperty('none', options=['on', 'off', 'none'])

  def __init__(self, **kw):
    super(Room, self).__init__(**kw)
    
  def get_points(self):
    x1, y1 = self.x, self.y
    x2, y2 = self.x, self.y + self.height
    x3, y3 = self.x + self.width, y2
    x4, y4 = x3, y1
    return [x1, y1, x2, y2, x3, y3, x4, y4]
    
  def draw(self):
    self.draw_background()
    self.draw_walls()
    self.draw_doors()
    self.draw_powerup()

  def draw_background(self):
    with self.canvas:
      if self.state == 'hidden'
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
    for wall in self.walls:
      if self.state == 'hidden':
        Color(0, .5, 0, 1)
        Line(points=self.get_points())
      else:
        if wall = 'full'
          Line()
        elif wall = 'gap':
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
    else if self.power == 'off':
      with self.canvas:
        Line(ellipse=)
