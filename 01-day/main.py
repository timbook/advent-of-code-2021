with open('input.txt', 'r') as f:
    lines = f.readlines()

measurements = [int(line.strip()) for line in lines]

increases = [
    1
    for a, b in zip(measurements[:-1], measurements[1:])
    if b - a > 0
]

n_increases = sum(increases)
print(f"A ::: Number of increases: {n_increases}")

# ============================================================================

lag0 = measurements[:-2]
lag1 = measurements[1:-1]
lag2 = measurements[2:]

measurements_lagged = [a + b + c for a, b, c in zip(lag0, lag1, lag2)]

increases_lagged = [
    1
    for a, b in zip(measurements_lagged[:-1], measurements_lagged[1:])
    if b - a > 0
]

n_increases_lagged = sum(increases_lagged)
print(f"B ::: Number of increases: {n_increases_lagged}")
