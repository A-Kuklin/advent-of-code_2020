group_answers = []
sum_answers = 0
with open('6.1.txt') as file:
    group_answer = set()
    for i, line in enumerate(file):
        line = line.strip()
        if line == '':
            sum_answers += len(group_answer)
            # print(len(group_answer), group_answer)
            group_answer = set()
        # print(line)
        group_answer.update(list(line))
sum_answers += len(group_answer)
print(sum_answers)
