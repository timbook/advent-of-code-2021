import math
import numpy as np

with open('input.txt', 'r') as f:
    data_raw = f.read()

data = np.array([int(n) for n in data_raw.strip().split(',')])

m = np.median(data)
fuel = np.sum(np.abs(data - m)).astype(int)

print(f"A ::: Fuel used: {fuel}")

L = lambda n: n*(n + 1)/2
b = np.mean(data)
fuel_down = np.sum(L(abs(data - math.floor(b))))
fuel_up = np.sum(L(abs(data - math.ceil(b))))
fuel = int(min(fuel_down, fuel_up))

print(f"B ::: Fuel used: {fuel}")
