class Passport:
    count = 0
    pos_list_1 = []

    def __init__(self, pos, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

        Passport.count += 1
        Passport.pos_list_1.append(pos)


dictionary = {}

with open('4.1.txt') as file:
    for i, line in enumerate(file):
        line = line.replace('\n', '')
        try:
            if len(line) == 0:
                passport = Passport(i, **dictionary)
                # print(i, dictionary)
                dictionary = {}
            dict_part = dict(sub_line.split(':') for sub_line in line.split(' '))
            dictionary.update(dict_part)
        except ValueError:
            dictionary = {}
        except TypeError as e:
            dictionary = {}
            print(f'{i} | {e}')
passport = Passport(999, **dictionary)

print(Passport.count)
print(len(Passport.pos_list_1), Passport.pos_list_1)
# print(len(pos_list_0), pos_list_0)
# diff = list(set(Passport.pos_list_1).symmetric_difference(set(pos_list_0)))
# print(diff)

