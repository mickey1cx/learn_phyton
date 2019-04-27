# https://stepik.org/lesson/21300/step/4?adaptive=true&unit=5101

import re


def split_decode_series(string):
    for count, letter in re.findall('(\d*)(\w)', string):
        yield 1 if count == '' else int(count), letter


def decode_series(series):
    result = ''
    for count, letter in series:
        result += letter * count
    return result


def rle_decode(string):
    series = split_decode_series('2a3bB')
    return decode_series(series)


print(rle_decode('2a3bB'))  # aabbbB
