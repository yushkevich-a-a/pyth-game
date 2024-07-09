# 🟩 ⬛ 🌊 🌳 ❤️ 🏥 ❤️ 🔴 🔥  🌩️ 🌥️ 🚁 

from map import Map
from helicopter import Helicopter

import time
import os
from pynput import keyboard

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10
MOVES={'w':(-1, 0),'d':(0, 1),'s':(1, 0),'a':(0, -1)}

map = Map(MAP_W, MAP_H)
helicop = Helicopter(MAP_W, MAP_H)

map.generate_forest(3, 9)
map.generate_river(10)
tick = 1

def proccess_key(key):
    global helicop
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helicop.moves(dx,dy)

listener = keyboard.Listener(
    on_press=None,
    on_release=proccess_key)
listener.start()



while True:
    os.system('cls' if os.name=='nt' else 'clear')
    print("TICK:", tick)
    map.print_map(helicop)
    time.sleep(TICK_SLEEP)
    tick += 1
    if (tick % TREE_UPDATE == 0 ):
        map.generate_tree()
    if (tick % FIRE_UPDATE == 0 ):
        map.update_fires()
