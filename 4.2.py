import re
from typing import ClassVar
from pydantic import BaseModel, validator


class Passport(BaseModel):
    pos: int = None
    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: str = None

    count: ClassVar[int] = 0
    pos_list_1: ClassVar[list] = []

    def __init__(self, **data):
        super().__init__(**data)
        Passport.count += 1
        Passport.pos_list_1.append(self.pos)

    # def __del__(self):
    #     Passport.count -= 1

    @validator('byr')
    def birth_year(cls, v):
        """ four digits; at least 1920 and at most 2002 """
        assert 1920 <= v <= 2002, f'birth_year error: 1920 ! _{v}_ ! 2002'
        return v

    @validator('iyr')
    def issue_year(cls, v):
        """ four digits; at least 2010 and at most 2020 """
        assert 2010 <= v <= 2020, f'issue_year error: 2010 ! _{v}_ ! 2020'
        return v

    @validator('eyr')
    def expiration_year(cls, v):
        """ four digits; at least 2020 and at most 2030 """
        assert 2020 <= v <= 2030, f'expiration_year error: 2020 ! _{v}_ ! 2030'
        return v

    @validator('hgt')
    def height(cls, v):
        """
        a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
        """
        if 'cm' in v:
            value = int(v.split('cm')[0])
            assert 150 <= value <= 193, f'height_cm error: 150 ! _{v}_ ! 193'
        elif 'in' in v:
            value = int(v.split('in')[0])
            assert 59 <= value <= 76, f'height_in error: 59 ! _{v}_ ! 76'
        else:
            raise ValueError('neither cm nor in')
        return v

    @validator('hcl')
    def hair_color(cls, v):
        """ a # followed by exactly six characters 0-9 or a-f """
        pattern = r"^#[0-9a-f]{6}$"
        assert re.match(pattern, v), f'hair_color error: {v}'
        return v

    @validator('ecl')
    def eye_color(cls, v):
        """ exactly one of: amb blu brn gry grn hzl oth """
        valid_params = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        assert v in valid_params, f'eye_color error: {v}'
        return v

    @validator('pid')
    def passport_id(cls, v):
        """ a nine-digit number, including leading zeroes """
        pattern = r"^[0-9]{9}$"
        assert re.match(pattern, v), f'passport_id error: {v}'
        return v


dictionary = {}

with open('4.1.txt') as file:
    for i, line in enumerate(file):
        line = line.strip()
        try:
            if len(line) == 0:
                dictionary['pos'] = i
                passport = Passport(**dictionary)
                dictionary = {}
            dict_part = dict(sub_line.split(':') for sub_line in line.split(' '))
            dictionary.update(dict_part)
        except Exception as e:
            dictionary = {}
            print(f'{i} | {e}')
# the last entry
passport = Passport(**dictionary)

print('* * *\n', Passport.count, Passport.pos_list_1)
