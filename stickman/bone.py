import math

from kivy.graphics.context_instructions import PopMatrix, PushMatrix, Rotate
from kivy.properties import NumericProperty
from kivy.uix.image import Image


class Bone(Image):

  angle = NumericProperty()

  def __init__(self, **kw):
    super(Bone, self).__init__(**kw)
    self.name = kw['name'] if 'name' in kw else None
    self.allow_stretch = True
    self.keep_ratio = False
    self.source = 'img/bone.png'
    self.next = []
    self.prev = None
    self.head = None
    self.tip = None
    self.bone_length = 0
    self.radius = None
    with self.canvas.before:
      PushMatrix()
      self.rotation = Rotate()
    with self.canvas.after:
      PopMatrix()    
    self.bind(pos=self.update, size=self.update, angle=self.rotate)
    
  def attach(self, bone):
    bone.prev = self
    self.next.append(bone)
    
  def attach_all(self, bones):
    for bone in bones:
      self.attach(bone)
      
  def rotate(self, *args):
    if self.prev:
      self.rotation.angle = self.prev.rotation.angle + self.angle
    else: self.rotation.angle = self.angle
    self.tip = self.get_tip_pos()
    for bone in self.next:
      self.coerce(bone)
      
  def update(self, *args):
    self.radius = self.width / 2
    self.bone_length = self.height - self.radius * 2 # approximate for head / tip radii
    self.head = self.x + self.radius, self.top - self.radius
    self.tip = self.get_tip_pos()
    # print 'head', self.head, self.prev, self.pos
    self.rotation.origin = self.head
    for bone in self.next:
      self.coerce(bone)
    
  def get_tip_pos(self):
    a = (self.rotation.angle - 90) * math.pi / 180
    dx = math.cos(a) * self.bone_length
    dy = math.sin(a) * self.bone_length
    return self.x + self.radius + dx, self.top - self.radius + dy
    
  def set_head_pos(self, pos):
    radius = self.width / 2
    head_x, head_y = pos
    self.pos = head_x - radius, head_y - radius - self.bone_length
    
  def coerce(self, bone):
    # print 'tip', self.get_tip_pos(), self.prev, self.pos
    bone.set_head_pos(self.tip)
    bone.rotate()