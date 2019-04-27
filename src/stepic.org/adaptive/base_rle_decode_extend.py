# https://stepik.org/lesson/21300/step/4?adaptive=true&unit=5101

import re


def split_decode_series(string):
    new_list = []
    for count, letter in re.findall('(\d*)(\w)', string):
        new_list.append((1 if count == '' else int(count), letter))
    return new_list


print(split_decode_series('2a3bB'))   # [(2, 'a'), (3, 'b'), (1, 'B')]
print(split_decode_series('a'))       # [(1, 'a')]
