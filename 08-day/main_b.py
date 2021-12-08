with open('data/input.txt', 'r') as f:
    lines = f.readlines()

class NumberDisplay:
    def __init__(self, line):
        lhs, rhs = line.strip().split(' | ')
        self.lhs = lhs.split()
        self.rhs = rhs.split()

    def solve_map(self):
        n2l = {}
        n2l[1] = [s for s in self.lhs if len(s) == 2][0]
        n2l[7] = [s for s in self.lhs if len(s) == 3][0]
        n2l[4] = [s for s in self.lhs if len(s) == 4][0]
        n2l[8] = [s for s in self.lhs if len(s) == 7][0]

        def n2set(n):
            return set(list(n2l[n]))

        def set2n(s):
            return list(s)[0]

        right_to_wrong = {}

        # a = 7 \ 1
        right_to_wrong['a'] = set2n(n2set(7) - n2set(1))

        # 9 = X st |X \ 4 \ 7| == 1
        n2l[9] = [s for s in self.lhs if len(set(list(s)) - n2set(4) - n2set(7)) == 1 and len(s) == 6][0]

        # g = 9 \ (4 u 7)
        right_to_wrong['g'] = set2n(n2set(9) - (n2set(4) | n2set(7)))

        # e = 8 \ 9
        right_to_wrong['e'] = set2n(n2set(8) - n2set(9))

        # 0 = X st (e in X) ^ (X u 7 == 7)
        n2l[0] = [
            s for s in self.lhs
            if (set(list(s)) | n2set(7)) == set(list(s)) and (right_to_wrong['e'] in s) and (len(s) == 6)
        ][0]

        # d = 8 \ 0
        right_to_wrong['d'] = set2n(n2set(8) - n2set(0))

        # b = 0 \ 7 \ e \ g
        right_to_wrong['b'] = set2n(n2set(0) - n2set(7) - set(right_to_wrong['e']) - set(right_to_wrong['g']))

        # 6 = X st (|X| == 6) & (d in X) ^ (e in X)
        n2l[6] = [
            s for s in self.lhs
            if (len(s) == 6) and (right_to_wrong['d'] in s) and (right_to_wrong['e'] in s)
        ][0]

        # c = 8 \ 6
        right_to_wrong['c'] = set2n(n2set(8) - n2set(6))

        # f = 8 = {abcdeg}
        right_to_wrong['f'] = set2n(n2set(8) - set(right_to_wrong.values()))

        wrong_to_right = {v:k for k,v in right_to_wrong.items()}

        self.n2l = n2l
        self.wrong_to_right = wrong_to_right
        self.right_to_wrong = right_to_wrong

    def str2number(self, s):
        n_converted = ''.join(sorted([self.wrong_to_right[char] for char in s]))
        return {
            'abcefg': '0',
            'cf': '1',
            'acdeg': '2',
            'acdfg': '3',
            'bcdf': '4',
            'abdfg': '5',
            'abdefg': '6',
            'acf': '7',
            'abcdefg': '8',
            'abcdfg': '9'
        }[n_converted]

    def solve(self):
        self.solve_map()
        rhs_n_list = [self.str2number(s) for s in self.rhs]
        return int(''.join(rhs_n_list))

nds = [NumberDisplay(line) for line in lines]
sols = sum(nd.solve() for nd in nds)
print(sols)
