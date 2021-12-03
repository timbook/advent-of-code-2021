with open('input.txt', 'r') as f:
    lines = f.readlines()

bits = [line.strip() for line in lines]

w = len(bits[0])
n = len(bits)

gamma = ''
epsilon = ''

for d in range(w):
    digits = [bit[d] for bit in bits]
    if digits.count('0') > digits.count('1'):
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

res_a = int(gamma, base=2)*int(epsilon, base=2)

print(f"A ::: Power consumption = {res_a}")

# Oxygen generator rating
oxygen_bits = bits.copy()
for d in range(w):
    digits = [bit[d] for bit in oxygen_bits]
    if digits.count('0') > digits.count('1'):
        mode = '0'
    elif digits.count('0') <= digits.count('1'):
        mode = '1'
    oxygen_bits = [bit for bit in oxygen_bits if bit[d] == mode]
    if len(oxygen_bits) == 1:
        break

oxygen_rating = oxygen_bits[0]

# CO2 scrubber rating
co2_bits = bits.copy()
for d in range(w):
    digits = [bit[d] for bit in co2_bits]
    if digits.count('0') > digits.count('1'):
        mode = '1'
    elif digits.count('0') <= digits.count('1'):
        mode = '0'
    co2_bits = [bit for bit in co2_bits if bit[d] == mode]
    if len(co2_bits) == 1:
        break

co2_rating = co2_bits[0]

# 4191984 too low
res_b = int(oxygen_rating, base=2)*int(co2_rating, base=2)
print(f"B ::: Life support rating = {res_b}")
