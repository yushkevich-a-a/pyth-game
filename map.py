
from utils import randbool, randcell , randcell2
from helicopter import Helicopter
from clouds import Clouds

# 0 - поле
# 1 - деревья
# 2 - вода
# 3 - больница
# 4 - улучшения
# 5 - огонь


TYPE_CELL = '🟩🌲🌊🏥🏡🔥'
UPGRADE_COST = 500
HEALING_COST = 1000

class Map(object):
  def __init__(self, w: int, h: int):
      self.w = w
      self.h = h
      self.cells = [[ 0 for i in range(w)] for i in range(h)]
      self.generate_forest(3, 9)
      self.generate_river(10)
      self.generate_river(10)
      self.generate_shop()
      self.generate_hospital()

  # генерация лесов
  def generate_forest(self, r, mxr):
     for i in range(self.h):
      for j in range(self.w):
        if randbool(r,mxr):
          self.cells[i][j]=1
  
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

  def generate_shop(self):
    c = randcell(self.w, self.h)
    cx, cy = c[0], c[1]
    self.cells[cx][cy] = 4

  def generate_hospital(self):
    c = randcell(self.w, self.h)
    cx, cy = c[0], c[1]
    if (self.cells[cx][cy] != 4):
      self.cells[cx][cy] = 3
    else:
      self.generate_hospital()
  
  # генерация пожаров
  def add_fire(self):
    c = randcell(self.w, self.h)
    cx, cy = c[0], c[1]
    if self.cells[cx][cy] == 1:
      self.cells[cx][cy] = 5

  def update_fires(self, helicopter: Helicopter):
    for i in range(self.h):
      for j in range(self.w):
        if (self.cells[i][j] == 5):
          if (helicopter.score >= 5 ): 
            helicopter.score -= 5
          self.cells[i][j] = 0
    for i in range(5):
      self.add_fire()


  def check_field(self, x, y):
    if x < 0 or y < 0 or x >= self.h or y >= self.w:
      return False
    return True
  
  def print_map(self, helicop: Helicopter, cloud: Clouds ):
    print('⬛' * (len(self.cells[0]) + 2))
    for ri in range(self.h):
      print('⬛', end='')
      for ci in range(self.w):
        cell = self.cells[ri][ci]
        clo = cloud.cells[ri][ci]
        if (clo == 1):
          print('🌥️ ', end='')
        elif (clo == 2):
          print('⚠️ ', end='')
        elif (ri == helicop.x and ci == helicop.y):
          print('🚁', end='')
        elif (cell >= 0 and cell < len(TYPE_CELL)):
          print(TYPE_CELL[cell], end='')
      print('⬛', )
    print('⬛' * (len(self.cells[0]) + 2))

  def process_helicopter(self, helicop: Helicopter, cloud: Clouds ):
    cell = self.cells[helicop.x][helicop.y]
    cell_light = cloud.cells[helicop.x][helicop.y]
    if (cell_light == 2):
      if( helicop.health <= 0):
        helicop.game_over()
        exit(0)
      helicop.health -= 1

    if (cell == 2):
      helicop.tank = helicop.mxtank
    if (cell == 5 and helicop.tank > 0):
      helicop.tank -=1
      self.cells[helicop.x][helicop.y] = 1
      helicop.score += 100
    if (cell == 4 and helicop.score >= UPGRADE_COST):
      helicop.mxtank +=1
      # self.cells[helicop.x][helicop.y] = 0
      helicop.score -= UPGRADE_COST
    if (cell == 3 and helicop.score >= HEALING_COST):
      helicop.health += 100
      # self.cells[helicop.x][helicop.y] = 0
      helicop.score -= HEALING_COST
      
  def export_data(self):
    return {"cells": self.cells }

  def import_data(self, data):
    self.cells = data["cells"]
