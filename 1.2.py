import re


with open('1.txt', 'r') as fp:
    data = fp.read()

""" 200 string'int' items """
raw_data = re.findall(r'\d+', data)
list_data = raw_data

res = 0
br = False
count = 0

""" count = 1 746 470 """
for a in list_data:
    for b in list_data:
        if a == b:
            continue
        for c in list_data:
            if b == c or a == c:
                continue
            x = int(a) + int(b) + int(c)
            count += 1
            if x == 2020:
                res = int(a) * int(b) * int(c)
                br = True
                break
        if br:
            break
    if br:
        break

print(res)
print(count)
