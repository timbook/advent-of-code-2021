import numpy as np
from collections import deque

with open('input.txt', 'r') as f:
    list_raw = f.read()

class FishList:
    def __init__(self, raw):
        self.data = np.array([int(n) for n in raw.strip().split(',')])
        self.day = 0

    def tick(self):
        self.day += 1
        n_zeros = np.sum(self.data == 0)
        self.data = np.where(self.data <= 6, (self.data - 1) % 7, self.data - 1)
        self.data = np.append(self.data, [8]*n_zeros)

fl = FishList(list_raw)
for i in range(80):
    fl.tick()
print(f"A ::: Total fish = {len(fl.data)}")

class FishListB:
    def __init__(self, raw):
        fish_list = [int(n) for n in raw.strip().split(',')]

        self.data = deque([0]*9)
        for i in range(7):
            self.data[i] = fish_list.count(i)

        self.day = 0

    def tick(self):
        self.day += 1
        n_zeros = self.data[0]
        self.data.rotate(-1)
        self.data[6] += n_zeros
    
fl = FishListB(list_raw)

for i in range(256):
    fl.tick()

print(f"B ::: Total fish = {sum(fl.data)}")
