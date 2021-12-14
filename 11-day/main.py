import numpy as np

lines = open('data/input.txt', 'r').readlines()

class Grid:
    def __init__(self, raw):
        self.grid = np.array([[int(n) for n in line.strip()] for line in raw])
        self.nrow, self.ncol = self.grid.shape
        self.total_flashes = 0
        self.steps = 0

    def increase(self):
        self.grid += 1

    def get_neighbors(self, r, c):
        neighbors_raw = [
            (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
            (r, c - 1),                 (r, c + 1),
            (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)
        ]
        neighbors = [
            (nb_r, nb_c) for nb_r, nb_c in neighbors_raw
            if 0 <= nb_r < self.nrow and 0 <= nb_c < self.ncol
        ]
        return neighbors

    def flash(self):
        flashed_already = []

        while True:
            # Find all new flashers
            rs, cs = np.where(self.grid > 9)
            flashers = [(r, c) for r, c in zip(rs, cs)]
            new_flashers = list(set(flashers) - set(flashed_already))
            self.total_flashes += len(new_flashers)
            if not new_flashers:
                break

            # Record that they have flashed this step
            flashed_already.extend(new_flashers)

            # Explode neighbors for each flasher
            to_explode = []
            for new_r, new_c in new_flashers:
                to_explode.extend(self.get_neighbors(new_r, new_c))                

            for r, c in to_explode:
                self.grid[r, c] += 1

        self.grid[self.grid > 9] = 0

    def check_sync(self):
        return np.all(self.grid == 0)

    def step(self):
        # Step 1: Increase all octopi
        self.increase()

        # Step 2: Flash
        self.flash()

        self.steps += 1

g = Grid(lines)
for i in range(100):
    g.step()

res_a = g.total_flashes
print(f"A ::: Total Flashes = {res_a}")

g = Grid(lines)
while not g.check_sync():
    g.step()

res_b = g.steps
print(f"B ::: Steps until synced = {res_b}")
