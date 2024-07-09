import os
# 🟩 ⬛ 🌊 🌳 ❤️ 🏥 ❤️ 🔴 🔥  🌩️ 🌥️ 🚁 


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
    print('⬛' * (len(self.cells) + 2))
    for line in self.cells:
      print('⬛', end='')
      for line in self.cells:
        print('🟩', end='')
      print('⬛', )
    print('⬛' * (len(self.cells) + 2))

    
  

map = Map(5, 10)

map.print_map()