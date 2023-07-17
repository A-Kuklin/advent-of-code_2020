from collections import Counter

group_answers = []
sum_answers = 0


def answers(answers_list):
    global sum_answers
    # print(answers_list)
    st = ''.join([''.join(x) for x in answers_list])
    d = Counter(st)
    for v in d.values():
        if v >= len(answers_list):
            sum_answers += 1
    # print(d)
    # print(f'sum_answers: {sum_answers}\n')


with open('6.1.txt') as file:
    gr_ans = []
    for i, line in enumerate(file):
        line = line.strip()
        if line == '':
            answers(gr_ans)
            gr_ans = []
            continue
        gr_ans.append([line])

answers(gr_ans)
print(sum_answers)
