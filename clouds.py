# 0 - безоблачно
# 1 - облачно
# 2 - гроза

class Clouds(object):
  def __init__(self, w: int, h: int):
    self.w = w
    self.h = h
    self.cells = [[ 0 for i in range(w)] for i in range(h)]

  def generate_cloud(self, c, mxc, g, mxg):
    
    return 0