a = len('....#...#####..##.#..##..#....#')
q = '....#...#####..##.#..##..#....#'
print(a)
print(q[4])
print(q)

raw_dict = {}
kek = 0
with open('3.txt') as file:
    for line in file:
        *value, key = line.split('\n')
        raw_dict[int(kek)] = value
        kek += 1

print(raw_dict.get(0)[0][4])

count = 0
trees = 0
val = 3
key = 3
for key in raw_dict:
    m = raw_dict[key][0][val]
    asd = raw_dict[key][0]
    if raw_dict[key][0][val] == '#':
        trees += 1
    # val += 3
    if key == 11:
        break

print(f'1 - 3: {raw_dict[1][0][3]}')
print(f'2 - 6: {raw_dict[2][0][6]}')
print(f'3 - 9: {raw_dict[3][0][9]}')
print(f'4 - 12: {raw_dict[4][0][12]}')
print(f'5 - 15: {raw_dict[5][0][15]}')
print(f'6 - 18: {raw_dict[6][0][18]}')
print(f'7 - 21: {raw_dict[7][0][21]}')

print(trees)
print(raw_dict)
print(len(raw_dict.keys()))