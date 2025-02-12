from utils import randbool

# 0 - безоблачно
# 1 - облачно
# 2 - гроза

class Clouds(object):
  def __init__(self, w: int, h: int):
    self.w = w
    self.h = h
    self.cells = [[ 0 for i in range(w)] for i in range(h)]

  def generate_cloud(self, c = 10, mxc = 100, g = 10, mxg = 100):
    for ri in range(self.h):
      for ci in range(self.w):
        if randbool(c, mxc):
          self.cells[ri][ci] = 1
          if randbool(g, mxg):
            self.cells[ri][ci] = 2
        else: 
          self.cells[ri][ci] = 0
  def export_data(self):
    return {"cells": self.cells }

  def import_data(self, data):
    self.cells = data["cells"]