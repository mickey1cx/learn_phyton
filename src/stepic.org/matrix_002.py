# https://stepik.org/lesson/3369/step/11?unit=952

count_numbers = int(input())
matrix = [[0] * count_numbers for row in range(count_numbers)]

direction_type = [[1, 0], [0, 1], [-1, 0], [0, -1]]
direction = 0
counter = 0
step = 0
x, y = 0, 0
dx, dy = 1, 0
len_direction = [count_numbers, count_numbers - 1]
len_type = 0

# 1

while counter < count_numbers ** 2:
    counter += 1
    matrix[y][x] = counter
    step += 1
    if len_direction[len_type] == step:
        len_direction[len_type] -= 1
        step = 0
        len_type = 0 if len_type == 1 else 1
        direction = (direction + 1) % 4
        dx = direction_type[direction][0]
        dy = direction_type[direction][1]
    x += dx
    y += dy

[([print(matrix[i][j], end=' ') for j in range(count_numbers)], print()) for i in range(count_numbers)]

# 2

while counter < count_numbers ** 2:
    counter += 1
    matrix[y][x] = counter
    new_x, new_y = x + dx, y + dy
    if (0 <= new_x < count_numbers) and (0 <= new_y < count_numbers) and matrix[new_y][new_x] == 0:
        x, y = new_x, new_y
    else:
        dx, dy = -dy, dx
    x += dx
    y += dy

[([print(matrix[i][j], end=' ') for j in range(count_numbers)], print()) for i in range(count_numbers)]