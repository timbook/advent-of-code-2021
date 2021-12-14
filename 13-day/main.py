import numpy as np
import matplotlib.pyplot as plt
import re

lines = open('data/input.txt', 'r').read()

points_raw, directions_raw = lines.split('\n\n')

points_str = points_raw.split('\n')
points = [(int(point.split(',')[0]), int(point.split(',')[1])) for point in points_str]

max_x = max(points, key=lambda t: t[0])[0]
max_y = max(points, key=lambda t: t[1])[1]

def proc_direction(line):
    var, n_str = re.findall('(x|y)=(\d+)', line)[0]
    return var, int(n_str)

directions = [proc_direction(direction) for direction in directions_raw.strip().split('\n')]

class Sheet:
    def __init__(self, max_x, max_y):
        self.grid = np.zeros((max_y + 1, max_x + 1))

    def add_point(self, p):
        self.grid[p[1], p[0]] = 1

    def __repr__(self):
        grid_str = np.where(self.grid == 0, '.', '#')
        rows = [''.join(grid_str[r, :]) for r in range(grid_str.shape[0])]
        return '\n'.join(rows)

    def fold(self, v, n):
        if v == 'x':
            self.fold_x(n)
        elif v == 'y':
            self.fold_y(n)

    def fold_y(self, n):
        T = self.grid[:n, :]
        B = self.grid[(n + 1):, :]

        B_prime = B[::-1, :]

        T_h = T.shape[0]
        B_h = B.shape[0]
        width = T.shape[1]

        if T_h == B_h:
            self.grid = T + B_prime
        else:
            spacer = np.zeros((abs(T_h - B_h), width))
            if T_h > B_h:
                B_prime = np.vstack([spacer, B_prime])
                self.grid = T + B_prime
            elif T_h < B_h:
                T_prime = np.vstack([spacer, T])
                self.grid = T_prime + B_prime

    def fold_x(self, n):
        L = self.grid[:, :n]
        R = self.grid[:, (n + 1):]
        L_prime = L[:, ::-1]

        L_w = L.shape[1]
        R_w = R.shape[1]

        if L_w == R_w:
            self.grid = R + L_prime
        else:
            import pdb; pdb.set_trace()

    def score(self):
        grid_binary = self.grid > 0
        return np.sum(grid_binary)

    def mirror(self):
        self.grid = self.grid[:, ::-1]

    def plot(self):
        g_plot = np.where(self.grid > 0, 1, 0)
        plt.imshow(g_plot)
        plt.show()

sh = Sheet(max_x, max_y)
for point in points:
    sh.add_point(point)

v0, n0 = directions[0]
sh.fold(v0, n0)
res_a = sh.score()
print(f"A ::: Visible dots = {res_a}")

for v, n in directions[1:]:
    sh.fold(v, n)

sh.mirror()
print("B ::: Folded manual:")
print(sh)

sh.plot()
