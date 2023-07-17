def indexes(letter, st_ind=0, end_ind=127):
    if letter in ['F', 'L']:
        st_ind = st_ind
        end_ind = st_ind + (end_ind - st_ind) // 2
    else:
        st_ind = st_ind + (end_ind - st_ind + 1) // 2
        end_ind = end_ind
    # print(letter, st_ind, end_ind)
    return st_ind, end_ind


with open('5.1.txt') as file:
    seat_list = []
    for i, line in enumerate(file):
        line = list(line.strip())
        # print(line)
        start = 0
        end = 127
        for g in line[:7]:
            start, end = indexes(g, start, end)
        if start == end:
            row = start
        start = 0
        end = 7
        for g in line[7:]:
            start, end = indexes(g, start, end)
        if start == end:
            column = start
        seat_id = row * 8 + column
        seat_list.append(seat_id)
        # print(f'row: {row}, column: {column}, seat ID: {seat_id}')
    seat_list.sort()
    st = seat_list[0]
    for i, s in enumerate(seat_list):
        if i == 0:
            continue
        ch = s - seat_list[i - 1]
        if ch != 1:
            print(f'may be my seat: {s - 1}')
    print(f'max seat ID: {max(seat_list)}')
