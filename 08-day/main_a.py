with open('data/input.txt', 'r') as f:
    lines = f.readlines()

def process_line(line):
    lhs, rhs = line.split(' | ')
    rhs_codes = rhs.strip().split()
    return len([n for n in rhs_codes if len(n) in [2, 3, 4, 7]])

print(sum(process_line(l) for l in lines))
