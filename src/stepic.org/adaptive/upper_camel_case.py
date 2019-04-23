# https://stepik.org/lesson/22776/step/2?adaptive=true&unit=5349

var = input()   # my_first_class
parts = var.split('_')

# 1
result = ''
for part in parts:
    result += part.capitalize()
print(result)

# 2
print(''.join(map(lambda x: x.capitalize(), parts)))

# 3
print(''.join(map(lambda x: x.capitalize(), var.split('_'))))

# 4 https://stepik.org/lesson/22776/step/2?adaptive=true&discussion=952481&thread=solutions&unit=5349
print("".join([x.capitalize() for x in var.split("_")]))

# 5 https://stepik.org/lesson/22776/step/2?adaptive=true&discussion=906114&thread=solutions&unit=5349
print(*var.title().split('_'), sep='')

# 6 https://stepik.org/lesson/22776/step/2?adaptive=true&discussion=901075&thread=solutions&unit=5349
print(var.title().replace('_', ''))
