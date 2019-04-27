# https://stepik.org/lesson/21977/step/2?adaptive=true&unit=5237

import collections

numbers = '14 8 0 3 14 2 0 3'   # input().split()

# 1

for key, value in collections.Counter(numbers.split()).items():
    if value > 1:
        print(key, end=' ')

# 2
print()
print(*[key for key, value in collections.Counter(numbers.split()).items() if value > 1])
