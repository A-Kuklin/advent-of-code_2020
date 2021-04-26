import re

raw_dict = {}
with open('2.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        *value, key = line.split(': ')
        if key in raw_dict.keys():
            key += '0'
        raw_dict[key] = value

valid_pass = 0
word = 0

for key, value in raw_dict.items():
    borders = re.findall('\d+', value[0])
    low = int(borders[0])
    high = int(borders[1])
    letter = re.findall('[a-z]', value[0])
    n = 0
    word += 1
    x = 0
    for i in str(key):
        n += 1
        if str(i) == letter[0]:
            if n == low:
                valid_pass += 1
                x = word
            if n == high and x == word:
                valid_pass -= 1
            if n == high and x != word:
                valid_pass += 1

print(valid_pass)
