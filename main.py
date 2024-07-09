# 🟩 ⬛ 🌊 🌳 ❤️ 🏥 ❤️ 🔴 🔥  🌩️ 🌥️ 🚁 

from map import Map
import time
import os

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

map = Map(MAP_W, MAP_H)

map.generate_forest(3, 9)
map.generate_river(10)
map.print_map()
tick = 1

while True:
    os.system('cls' if os.name=='nt' else 'clear')
    print("TICK:", tick)
    map.print_map()
    time.sleep(TICK_SLEEP)
    tick += 1
    if (tick % TREE_UPDATE == 0 ):
        map.generate_tree()
    if (tick % FIRE_UPDATE == 0 ):
        map.update_fires()
