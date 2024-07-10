from utils import randcell

class Helicopter(object):
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.w = w
        self.h = h
        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.health = 20
        
    
    def moves(self, dx, dy):
        nx, ny = self.x + dx, self.y + dy
        if (nx >= 0 and nx < self.h and ny >= 0 and ny < self.w):
            self.x = nx
            self.y = ny

    def print_status(self):
        print('🧺 ', self.tank, '/',self.mxtank, sep='', end=" | ")
        print('🏆 ', self.score, end=" | ")
        print('💚 ', self.health)

    def game_over(self):

        st = f'X   CAME OVER! YOUR SCORE IS {self.score}   X'
        print('X' * len(st))
        print('X', ' ' * (len(st) - 2),'X', sep='')
        print(st)
        print('X', ' ' * (len(st) - 2), 'X', sep='')
        print('X' * len(st))

    def export_data(self):
        data = {
        "x": self.x,
        "y": self.y,
        "tank": self.tank,
        "mxtank": self.mxtank,
        "score": self.score,
        "health": self.health,
        }
        return data
    
    def import_data(self, data):
         self.x = data["x"]
         self.y = data["y"]
         self.tank = data["tank"]
         self.mxtank = data["mxtank"]
         self.score = data["score"]
         self.health = data["health"]