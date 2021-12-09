import numpy as np

with open('data/input.txt', 'r') as f:
    lines = f.readlines()

grid = np.array([[int(n) for n in line.strip()] for line in lines])
nrow, ncol = grid.shape

low_points = []
for r in range(nrow):
    for c in range(ncol):
        neighbors = []
        if r >= 1:
            neighbors.append(grid[r - 1, c])
        if r <= nrow - 2:
            neighbors.append(grid[r + 1, c])
        if c >= 1:
            neighbors.append(grid[r, c - 1])
        if c <= ncol - 2:
            neighbors.append(grid[r, c + 1])

        if grid[r, c] < min(neighbors):
            low_points.append((grid[r, c], r, c))

res_a = sum(n + 1 for n, r, c in low_points)
print(f"A ::: Number of low points = {res_a}")

class Node:
    def __init__(self, value, r, c):
        self.value = value
        self.r = r
        self.c = c
        self.neighbors = []
        self.discovered = False

    def add_nb(self, nb):
        self.neighbors.append(nb)

    def __repr__(self):
        return str(self.value)

# Create nodes
nodes = {}
for r in range(nrow):
    for c in range(ncol):
        nodes[(r, c)] = Node(grid[r, c], r, c)

# Add node neighbors
for r in range(nrow):
    for c in range(ncol):
        node = nodes[(r, c)]
        if r >= 1:
            node.add_nb(nodes[(r - 1, c)])
        if r <= nrow - 2:
            node.add_nb(nodes[(r + 1, c)])
        if c >= 1:
            node.add_nb(nodes[(r, c - 1)])
        if c <= ncol - 2:
            node.add_nb(nodes[(r, c + 1)])

def explore(X):
    nbs = [nb for nb in X.neighbors if nb.value != 9 and not nb.discovered]
    global size
    size += len(nbs)

    for nb in nbs:
        nb.discovered = True

    for nb in nbs:
        explore(nb)

sizes = []
for lp in low_points:
    _, r, c = lp
    if not nodes[(r, c)].discovered:
        size = 1
        nodes[(r, c)].discovered = True
        explore(nodes[(r, c)])
    sizes.append(size)

sizes_sorted = sorted(sizes)[-3:]
res_b = sizes_sorted[0]*sizes_sorted[1]*sizes_sorted[2]
print(f"B ::: Product of largest 3 basins = {res_b}")
