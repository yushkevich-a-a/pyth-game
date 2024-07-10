# 🟩 ⬛ 🌊 🌳 ❤️ 🏥 ❤️💡⚡︎ 🏡 🔥 ⚡ 💥 ⚡️⚡️  ⚡ 🌥️ 🚁 🧺 🏆


from map import Map
from clouds import Clouds
from helicopter import Helicopter

import time
import os
import json
from pynput import keyboard

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
UPDATE_CLOUD = 75
MAP_W, MAP_H = 20, 10
MOVES={'w':(-1, 0),'d':(0, 1),'s':(1, 0),'a':(0, -1)}

map = Map(MAP_W, MAP_H)
cloud = Clouds(MAP_W, MAP_H)
helicop = Helicopter(MAP_W, MAP_H)
tick = 1

def proccess_key(key):
    global helicop, tick, cloud, map
    try: 
        c = key.char.lower()
        if c in MOVES.keys():
            dx, dy = MOVES[c][0], MOVES[c][1]
            helicop.moves(dx,dy)
        elif c == 'f':
            data = {
                "helicopter": helicop.export_data(),
                "map": map.export_data(),
                "clouds": cloud.export_data(),
                'tick': tick
            }
            with open('level.json', 'w') as lvl:
                json.dump(data, lvl)
        elif c == 'g':
            with open('level.json', 'r') as lvl:
                data = json.load(lvl)
                helicop.import_data(data["helicopter"])
                map.import_data(data["map"])
                cloud.import_data(data["clouds"])
                tick = data["tick"] or 1
    except AttributeError:
        return

listener = keyboard.Listener(
    on_press=None,
    on_release=proccess_key)
listener.start()



while True:
    os.system('cls' if os.name=='nt' else 'clear')
    map.process_helicopter(helicop, cloud)
    helicop.print_status()
    map.print_map(helicop, cloud)
    print("TICK:", tick)

    time.sleep(TICK_SLEEP)
    tick += 1
    if (tick % TREE_UPDATE == 0 ):
        map.generate_tree()
    if (tick % FIRE_UPDATE == 0 ):
        map.update_fires()
    if (tick % UPDATE_CLOUD == 0 ):
        cloud.generate_cloud()
