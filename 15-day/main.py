import numpy as np
import networkx as nx
from itertools import product

#  lines = open('data/sample-input.txt', 'r').readlines()
lines = open('data/input.txt', 'r').readlines()

arr = np.array([[int(n) for n in line.strip()] for line in lines])
nrow, ncol = arr.shape

# Instantiate graph
G = nx.DiGraph()

# Add edges with weights
for r, c in product(range(nrow), range(ncol)):
    nbs = [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]
    nbs = [(r, c) for r, c in nbs if 0 <= r < nrow and 0 <= c < ncol]
    for nb_r, nb_c in nbs:
        G.add_edge((r, c), (nb_r, nb_c), weight=arr[nb_r, nb_c])

src = (0, 0)
dest = (nrow - 1, ncol - 1)
p = nx.dijkstra_path(G, src, dest, weight='weight')
sol = sum(arr[r, c] for r, c in p) - arr[src[0], src[1]]
print(f"SHORTEST PATH: {sol}")

# =============================================================================

arr_big = np.vstack([
    np.hstack([arr    , arr + 1, arr + 2, arr + 3, arr + 4]),
    np.hstack([arr + 1, arr + 2, arr + 3, arr + 4, arr + 5]),
    np.hstack([arr + 2, arr + 3, arr + 4, arr + 5, arr + 6]),
    np.hstack([arr + 3, arr + 4, arr + 5, arr + 6, arr + 7]),
    np.hstack([arr + 4, arr + 5, arr + 6, arr + 7, arr + 8])
])

arr_big = np.where(arr_big > 9, arr_big - 9, arr_big)
nrow, ncol = arr_big.shape

# Instantiate graph
G = nx.DiGraph()

# Add edges with weights
for r, c in product(range(nrow), range(ncol)):
    nbs = [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]
    nbs = [(r, c) for r, c in nbs if 0 <= r < nrow and 0 <= c < ncol]
    for nb_r, nb_c in nbs:
        G.add_edge((r, c), (nb_r, nb_c), weight=arr_big[nb_r, nb_c])

src = (0, 0)
dest = (nrow - 1, ncol - 1)
p = nx.dijkstra_path(G, src, dest, weight='weight')
sol = sum(arr_big[r, c] for r, c in p) - arr_big[src[0], src[1]]
print(f"SHORTEST PATH: {sol}")
