import numpy as np

with open('input.txt', 'r') as f: lines = f.readlines()

draws = [int(line) for line in lines[0].split(',')]

boards_raw = ''.join(lines[2:]).strip().split('\n\n')

class Board:
    def __init__(self, raw):
        board_list = [[int(n) for n in line.strip().split()] for line in raw.split('\n')]
        self.board = np.array(board_list)
        self.marks = np.zeros_like(self.board, dtype=bool)

    def mark(self, n):
        r, c = np.where(self.board == n)
        if len(r) > 0:
            self.marks[r[0], c[0]] = True

    def check(self):
        rows = [all(self.marks[i,:]) for i in range(5)]
        cols = [all(self.marks[:,i]) for i in range(5)]
        return any(rows) or any(cols)

    def score(self):
        return np.sum(self.board * (1 - self.marks))

boards = [Board(b) for b in boards_raw]

for draw in draws:

    # Mark all boards
    _ = [b.mark(draw) for b in boards]

    # Check if any boards are won    
    winning_board = [b for b in boards if b.check()]
    if winning_board:
        final_draw = draw
        final_score = winning_board[0].score()
        break

print(f"A ::: Score = {final_draw*final_score}")

boards = [Board(b) for b in boards_raw]

for draw in draws:

    # Mark all boards
    _ = [b.mark(draw) for b in boards]

    if len(boards) > 1:
        # Drop completed boards
        boards = [b for b in boards if not b.check()]

    if len(boards) == 1:
        if boards[0].check():
            final_draw = draw
            final_score = boards[0].score()
            break

print(f"B ::: Score = {final_draw*final_score}")
