with open('input.txt', 'r') as f:
    moves_raw = f.readlines()

class Submarine:
    def __init__(self):
        self.depth = 0
        self.position = 0
        self.aim = 0

    def process_move_a(self, move):
        direction, distance = move.strip().split()

        if direction == 'forward':
            self.position += int(distance)

        elif direction == 'down':
            self.depth += int(distance)

        elif direction == 'up':
            self.depth -= int(distance)

    def process_move_b(self, move):
        direction, distance = move.strip().split()

        if direction == 'forward':
            self.position += int(distance)
            self.depth += self.aim*int(distance)

        elif direction == 'down':
            self.aim += int(distance)

        elif direction == 'up':
            self.aim -= int(distance)

sub = Submarine()
for move in moves_raw:
    sub.process_move_a(move)

res_a = sub.position*sub.depth

print(f"A ::: Result = {res_a}")

sub = Submarine()
for move in moves_raw:
    sub.process_move_b(move)

res_b = sub.position*sub.depth

print(f"B ::: Result = {res_b}")

