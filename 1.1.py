import re


with open('1.txt', 'r') as fp:
    data = fp.read()

""" 200 string'int' items """
raw_data = re.findall(r'\d+', data)
list_data = raw_data

res = 0
br = False
count = 0

""" count = 6 661 """
for i in range(len(list_data)):
    for y in range(len(list_data)):
        x = int(list_data[i]) + int(list_data[y])
        count += 1
        if x == 2020:
            res = int(list_data[i]) * int(list_data[y])
            br = True
            break
    del list_data[i]
    if br:
        break

""" count = 14 527 """
# for i in list_data:
#     for y in list_data:
#         x = int(i) + int(y)
#         count += 1
#         if x == 2020:
#             res = int(i) * int(y)
#             br = True
#             break
#     if br:
#         break

print(res)
print(count)
