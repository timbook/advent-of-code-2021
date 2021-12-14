import numpy as np

with open('data/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

class Code:
    r2l_map = {')': '(', ']': '[', '}': '{', '>': '<'}
    l2r_map = {v:k for k,v in r2l_map.items()}

    def __init__(self, line):
        self.data = list(line)
        self.corrupted = False

    def solve_a(self):
        self.stack = ['']
        for char in self.data:
            if char in '([{<':
                self.stack.append(char)
            elif char in ')]}>':
                if self.r2l_map[char] != self.stack[-1]:
                    self.corrupted = True
                    self.offending_char = char
                    break
                elif self.r2l_map[char] == self.stack[-1]:
                    self.stack.pop()

    def solve_b(self):
        self.stack = self.stack[1:]
        self.autocomplete = []
        for lbracket in self.stack[::-1]:
            self.autocomplete.append(self.l2r_map[lbracket])

    def score_b(self):
        point_map = {')': 1, ']': 2, '}': 3, '>': 4}
        score = 0
        for char in self.autocomplete:
            score *= 5
            score += point_map[char]
        return score

codes = [Code(line) for line in lines]

_ = [code.solve_a() for code in codes]
offending_chars = [code.offending_char for code in codes if code.corrupted]

point_map = {')': 3, ']': 57, '}': 1197, '>': 25137}

res_a = sum(point_map[char] for char in offending_chars)
print(f"A ::: Total points = {res_a}")

codes_incomplete = [code for code in codes if not code.corrupted]
_ = [code.solve_b() for code in codes]

scores_b = [code.score_b() for code in codes_incomplete]
res_b = int(np.median(scores_b))
print(f"B ::: Total points = {res_b}")
