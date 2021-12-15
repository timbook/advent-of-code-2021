lines = open('data/input.txt', 'r').readlines()

init_polymer = lines[0].strip()

rules_raw = lines[2:]
rules_tup = [line.strip().split(' -> ') for line in rules_raw]
rule_map = {k:v for k,v in rules_tup}
letters = list(set([v for k, v in rule_map.items()]))

class Polymer:
    def __init__(self, starting_polymer):
        pairs = list(zip(starting_polymer[:-1], starting_polymer[1:]))
        self.data = {''.join(pair): pairs.count(pair) for pair in set(pairs)}
        self.counts = {letter: starting_polymer.count(letter) for letter in letters}


    def expand(self):
        new_data = {}
        for pair, n in self.data.items():
            output = rule_map[pair]

            self.counts[output] += n
            
            lhs = pair[0] + output
            rhs = output + pair[1]

            new_data[lhs] = new_data.get(lhs, 0) + n
            new_data[rhs] = new_data.get(rhs, 0) + n

        self.data = new_data

    def score(self):
        l_min = min(self.counts, key=lambda d: self.counts[d])
        l_max = max(self.counts, key=lambda d: self.counts[d])
        min_count = self.counts[l_min]
        max_count = self.counts[l_max]
        return max_count - min_count

poly = Polymer(init_polymer)

for _ in range(10):
    poly.expand()

res_a = poly.score()
print(f"A ::: After 10 steps = {res_a}")

for _ in range(30):
    poly.expand()

res_b = poly.score()
print(f"B ::: After 40 steps = {res_b}")
