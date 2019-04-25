# https://stepik.org/lesson/21300/step/2?adaptive=true&unit=5101

import re

data = input()  # '3ab4c2CaB'
l = re.findall('((\d*)(\w))', data)
for i in l:
    print(i[2] * (1 if i[1] == '' else int(i[1])), end='')  # aaabccccCCaB

# 2
print()
for full, count, letter in l:
    print(letter * (1 if count == '' else int(count)), end='')

# 3 !!!
# ((\d*)(\w)) = group, [0]full, [1]count, [2]letter
# (\d*)(\w)) = group, [0]count, [1]letter
l = re.findall('(\d*)(\w)', data)
print()
for count, letter in l:
    print(letter * (1 if count == '' else int(count)), end='')

# https://stepik.org/lesson/21300/step/2?adaptive=true&discussion=962418&thread=solutions&unit=5101
# yield sample
