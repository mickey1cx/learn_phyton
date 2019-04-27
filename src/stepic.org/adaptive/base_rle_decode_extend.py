# https://stepik.org/lesson/21300/step/4?adaptive=true&unit=5101

import re


def split_decode_series(string):
    for count, letter in re.findall('(\d*)(\w)', string):
        yield 1 if count == '' else int(count), letter


print(list(split_decode_series('2a3bB')))   # [(2, 'a'), (3, 'b'), (1, 'B')]
print(list(split_decode_series('a')))       # [(1, 'a')]
