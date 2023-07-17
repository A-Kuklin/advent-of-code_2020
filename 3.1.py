STEP = 3
n_slide = 1
n_trees = 0
pos = 0

with open('3.0.txt') as file:
    for line in file:
        value = line.replace('\n', '')
        long_value = value * n_slide
        try:
            position = long_value[pos]
        except IndexError:
            n_slide += 1
            position = (value * n_slide)[pos]
        print(f'{pos} / {position}: {value}')
        pos += STEP
        n_trees += 1 if position == '#' else 0

# with open('3.txt') as file:
#     for line in file:
#         value = line.replace('\n', '')
#         long_value = value * n_slide
#         try:
#             position = long_value[pos]
#         except IndexError:
#             n_slide += 1
#             position = (value * n_slide)[pos]
#         # print(f'{pos:02} / {position}: {value}')
#         pos += STEP
#         n_trees += 1 if position == '#' else 0

print(f'Количество деревьев: {n_trees}')
