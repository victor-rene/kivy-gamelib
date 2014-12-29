import random, sys

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout

from bone import Bone


class StickMan(RelativeLayout):

  def __init__(self, **kw):
    super(StickMan, self).__init__(**kw)
    self.head = Bone(size_hint=(.1, .1), name='head')
    self.head.source = 'img/head.png'
    self.neck = Bone(size_hint=(.02, .1), name='neck')
    self.trunk = Bone(size_hint=(.04, .2), name='trunk')
    self.l_arm = Bone(size_hint=(.04, .15), name='l_arm')
    self.l_forearm = Bone(size_hint=(.04, .15), name='l_forearm')
    self.r_arm = Bone(size_hint=(.04, .15), name='r_arm')
    self.r_forearm  = Bone(size_hint=(.04, .15), name='l_forearm')
    self.l_thigh = Bone(size_hint=(.04, .2), name='l_thigh')
    self.l_leg = Bone(size_hint=(.04, .2), name='l_leg')
    self.r_thigh = Bone(size_hint=(.04, .2), name='r_thigh')
    self.r_leg = Bone(size_hint=(.04, .2), name='r_leg')
    self.head.attach(self.neck)
    self.neck.attach_all([self.trunk, self.l_arm, self.r_arm])
    self.l_arm.attach(self.l_forearm)
    self.r_arm.attach(self.r_forearm)
    self.trunk.attach_all([self.l_thigh, self.r_thigh])
    self.l_thigh.attach(self.l_leg)
    self.r_thigh.attach(self.r_leg)
    self.bones = [self.head, self.neck, self.trunk,
      self.l_arm, self.r_arm, self.l_forearm, self.r_forearm,
      self.l_thigh, self.r_thigh, self.l_leg, self.r_leg]
    for bone in self.bones:
      self.add_widget(bone)
    self.anims = {'flex': self.flex, 'high_kick': self.high_kick,
      'high_punch': self.high_punch}
    self.bind(pos=self.update, size=self.update)
    Clock.schedule_interval(self.constraint, 0.01)
    
  def constraint(self, dt):
    """ Applies gravity """
    min_x = sys.maxint
    min_y = sys.maxint
    max_x = - sys.maxint
    max_y = - sys.maxint
    for bone in self.bones:
      if bone.tip:
        min_x = min(bone.tip[0], min_x)
        min_y = min(bone.tip[1], min_y)
        max_x = max(bone.tip[0], max_x)
        max_y = max(bone.tip[1], max_y)
      if bone.head:
        min_x = min(bone.head[0], min_x)
        min_y = min(bone.head[1], min_y)
        max_x = max(bone.head[0], max_x)
        max_y = max(bone.head[1], max_y)
    # print min_x, min_y, max_x, max_y
    self.head.y -= min_y
    self.head.center_x = self.width / 2
    for bone in self.bones:
      if bone.name == self.anchor:
        self.head.center_x += self.width / 2 - bone.tip[0]
        print bone.tip
        # self.head.center_x += bone.tip[0]
    # self.neck.x -= min_x
    # if min_y < 0:
      # self.neck.y -= min_y
    
  def update(self, *args):
    pass
    # self.head.center_x = self.width / 2
    # self.neck.y = self.height / 2

  def flex(self):
    self.anim_done = 0
    self.anim_max = 8
    self.curr_anim = 'flex'
    self.anchor = None
    anim = Animation(angle=90)
    anim.start(self.r_arm)
    anim.start(self.r_forearm)
    anim.start(self.r_thigh)
    anim.start(self.l_leg)
    anim.bind(on_complete=self.inc_anims)
    anim = Animation(angle=-90)
    anim.start(self.l_arm)
    anim.start(self.l_forearm)
    anim.start(self.l_thigh)
    anim.start(self.r_leg)
    anim.bind(on_complete=self.inc_anims)
    
  def high_punch(self):
    self.anim_done = 0
    self.anim_max = 6
    self.curr_anim = 'high_punch'
    self.anchor = 'r_leg'
    anim = Animation(angle=45)
    anim.start(self.l_arm)
    anim.bind(on_complete=self.inc_anims)
    anim = Animation(angle=-90)
    anim.start(self.r_arm)
    anim.bind(on_complete=self.inc_anims)
    anim = Animation(angle=90)
    anim.start(self.l_leg)
    anim.bind(on_complete=self.inc_anims)
    anim = Animation(angle=60)
    anim.start(self.r_thigh)
    anim.bind(on_complete=self.inc_anims)
    anim = Animation(angle=-90)
    anim.start(self.l_thigh)
    anim.start(self.l_forearm)
    anim.bind(on_complete=self.inc_anims)
  
  def high_kick(self):
    self.anim_done = 0
    self.anim_max = 6
    self.curr_anim = 'high_kick'
    self.anchor = 'l_leg'
    anim = Animation(angle=90)
    anim.start(self.l_forearm)
    anim.start(self.r_arm)
    anim.bind(on_complete=self.inc_anims)
    anim = Animation(angle=-45)
    anim.start(self.l_arm)
    anim.bind(on_complete=self.inc_anims)
    anim = Animation(angle=60)
    anim.start(self.trunk)
    anim.bind(on_complete=self.inc_anims)
    anim = Animation(angle=60)
    anim.start(self.r_thigh)
    anim.bind(on_complete=self.inc_anims)
    anim = Animation(angle=-60)
    anim.start(self.l_thigh)
    anim.bind(on_complete=self.inc_anims)
    
  def reset(self):
    self.anim_done = 0
    self.anim_max = 9
    self.curr_anim = 'reset'
    anim = Animation(angle=0)
    anim.start(self.trunk)
    anim.start(self.r_arm)
    anim.start(self.r_forearm)
    anim.start(self.r_thigh)
    anim.start(self.l_leg)
    anim.start(self.l_arm)
    anim.start(self.l_forearm)
    anim.start(self.l_thigh)
    anim.start(self.r_leg)
    anim.bind(on_complete=self.inc_anims)
    
  def inc_anims(self, *args):
    self.anim_done += 1
    if self.anim_done == self.anim_max:
      self.anim_done = 0
      if self.curr_anim != 'reset':
        self.reset()
      else:
        k = random.choice(self.anims.keys())
        self.anims[k]()
