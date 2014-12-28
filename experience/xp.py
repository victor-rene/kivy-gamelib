def calc_level(xp, xp_levels):
  lvl = 1
  for xp_level in xp_levels:
    xp -= xp_level
    if xp < 0:
      break
    else: lvl += 1
  return lvl
  
def init_xp(obj):
  obj.xp = 0
  obj.xp_levels = [i * 100 for i in range(1, 10)]
  obj.xp_max = sum(xp_levels)
  obj.level_max = 10
  obj.level = 1
  
def upd_xp(obj):
  obj.level = calc_level(obj.xp, obj.xp_levels)
  
def inc_xp(obj, value):
  obj.xp += value
  upd_xp(obj)
  
def set_xp(obj, value):
  obj.xp = value
  upd_xp(obj)
