
from utils import randbool, randcell , randcell2
from helicopter import Helicopter
# 0 - поле
# 1 - деревья
# 2 - вода
# 3 - больница
# 4 - улучшения
# 5 - огонь


TYPE_CELL = '🟩🌳🌊🏥🔴🔥'


class Map(object):
  def __init__(self, w: int, h: int):
      self.w = w
      self.h = h
      self.cells = [[ 0 for i in range(w)] for i in range(h)]

  # генерация лесов
  def generate_forest(self, r, mxr):
     for i in range(self.h):
      for j in range(self.w):
        if randbool(r,mxr):
          self.cells[i][j]=1
  
  
  # генерация пожаров
  def add_fire(self):
    c = randcell(self.w, self.h)
    cx, cy = c[0], c[1]
    if self.cells[cx][cy] == 1:
      self.cells[cx][cy] = 5

  def update_fires(self):
    for i in range(self.h):
      for j in range(self.w):
        if (self.cells[i][j] == 5):
          self.cells[i][j] = 0
    for i in range(5):
      self.add_fire()

  # генерация деревьев
  def generate_tree(self):
    c = randcell(self.w, self.h)
    cx, cy = c[0], c[1]
    if self.cells[cx][cy] == 0:
      self.cells[cx][cy] = 1

  # генерация рек
  def generate_river(self, l):
      rc = randcell(self.w, self.h)
      rx, ry = rc[0], rc[1]
      self.cells[rx][ry] = 2
      while l > 0:
        print(rx, ry)
        rc2 = randcell2(rx, ry)
        rx2, ry2 = rc2[0], rc2[1]
        if self.check_field(rx2, ry2) :
           self.cells[rx2][ry2] = 2
           rx, ry = rx2, ry2 
           l -= 1

  def check_field(self, x, y):
    if x < 0 or y < 0 or x >= self.h or y >= self.w:
      return False
    return True
  
  def print_map(self, helicop: Helicopter):
    print('⬛' * (len(self.cells[0]) + 2))
    for ri in range(self.h):
      print('⬛', end='')
      for ci in range(self.w):
        cell = self.cells[ri][ci]
        if (ri == helicop.x and ci == helicop.y):
          print('🚁', end='')
        elif (cell >= 0 and cell < len(TYPE_CELL)):
          print(TYPE_CELL[cell], end='')
      print('⬛', )
    print('⬛' * (len(self.cells[0]) + 2))