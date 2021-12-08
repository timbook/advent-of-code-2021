import numpy as np
from collections import deque

with open('input.txt', 'r') as f:
    list_raw = f.read()

class FishList:
    def __init__(self, raw):
        self.day = 0
        fish_list = [int(n) for n in raw.strip().split(',')]
        self.data = deque([0]*9)
        for i in range(7):
            self.data[i] = fish_list.count(i)

    def tick(self):
        self.day += 1
        n_zeros = self.data[0]
        self.data.rotate(-1)
        self.data[6] += n_zeros

fl = FishList(list_raw)
for i in range(80):
    fl.tick()
print(f"A ::: Total fish = {sum(fl.data)}")

fl = FishList(list_raw)
for i in range(256):
    fl.tick()

print(f"B ::: Total fish = {sum(fl.data)}")
