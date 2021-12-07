import re
import numpy as np

#  with open('input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()

class Vent:
    def __init__(self, raw):
        x1, y1, x2, y2 = re.findall('(\d+),(\d+) -> (\d+),(\d+)', raw.strip())[0]
        self.raw = raw.strip()
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

    def min_x(self):
        return min(self.x1, self.x2)

    def min_y(self):
        return min(self.y1, self.y2)

    def max_x(self):
        return max(self.x1, self.x2)

    def max_y(self):
        return max(self.y1, self.y2)

    def __repr__(self):
        return self.raw

class Grid:
    def __init__(self, x_max, y_max):
        self.grid = np.zeros((y_max + 1, x_max + 1), dtype=int)

    def add_vent(self, vent):
        x_min, x_max = min(vent.x1, vent.x2), max(vent.x1, vent.x2)
        y_min, y_max = min(vent.y1, vent.y2), max(vent.y1, vent.y2)

        try:
            slope = -(vent.y2 - vent.y1) / (vent.x2 - vent.x1)
        except:
            slope = 0

        # If vertical or horizontal
        if vent.x1 == vent.x2 or vent.y1 == vent.y2:
            self.grid[
                np.arange(y_min, y_max + 1),
                np.arange(x_min, x_max + 1)
            ] += 1

        # Otherwise, if at +45 angle
        elif slope > 0:
            d = vent.max_x() - vent.min_x()
            for i in range(d + 1):
                self.grid[
                    vent.max_y() - i,
                    vent.min_x() + i
                ] += 1

        # Vent at -45 angle
        else:
            d = vent.max_x() - vent.min_x()
            for i in range(d + 1):
                self.grid[
                    vent.min_y() + i,
                    vent.min_x() + i
                ] += 1

    def count_overlaps(self):
        return len(self.grid[self.grid > 1])

vents = [Vent(line) for line in lines]

x_max = max(vents, key=lambda v: v.max_x()).max_x()
y_max = max(vents, key=lambda v: v.max_y()).max_y()

grid = Grid(x_max, y_max)
for vent in vents:
    if vent.x1 == vent.x2 or vent.y1 == vent.y2:
        grid.add_vent(vent)
n_overlap_a = grid.count_overlaps()
print(f"A ::: Number of overlaps: {n_overlap_a}")

grid = Grid(x_max, y_max)
for vent in vents:
    grid.add_vent(vent)
n_overlap_b = grid.count_overlaps()
print(f"B ::: Number of overlaps: {n_overlap_b}")
