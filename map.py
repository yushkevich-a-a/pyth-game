import os
# 🟩 ⬛ 🌊 🌳 ❤️ 🏥 ❤️ 🔴 🔥  🌩️ 🌥️ 🚁 

TYPE_CELL = '🟩🌳🌊🏥'

clear = lambda: os.system('clear')

class Map(object):
  def __init__(self, w: int, h: int):
      self.cells = [[ 0 for i in range(w)] for i in range(h)]

  # генерация лесов
  # def generate_forest(self):
  #    return 0
  
  # генерация пожаров
  # def generate_fire(self):
  #    return 0
  
  def print_map(self):
    clear()
    print('⬛' * (len(self.cells[0]) + 2))
    for line in self.cells:
      print('⬛', end='')
      for i in line:
        print(TYPE_CELL[i], end='')
      print('⬛', )
    print('⬛' * (len(self.cells[0]) + 2))

    
  

map = Map(10, 10)

map.cells[2][4] = 1
map.cells[3][5] = 2
map.cells[5][5] = 3

map.print_map()