# https://stepik.org/lesson/21975/step/2?adaptive=true&unit=5235

numbers = '5 8 2 7 8 8 2 4'.split() # input()
search_value = '8'
result = []
for i in range(len(numbers)):
    if numbers[i] == search_value:
        result.append(i)
if len(result) > 0:
    print(*result)
else:
    print('None')

# 2
result = []
for idx, value in enumerate(numbers):
    if value == search_value:
        result.append(idx)
print(' '.join(str(value) for value in result) or None)

# 3
print(' '.join([str(idx) for idx, value in enumerate(numbers) if value == search_value]) or None)
