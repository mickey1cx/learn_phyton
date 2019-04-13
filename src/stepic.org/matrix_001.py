# https://stepik.org/lesson/3369/step/10?unit=952

# string_list = ["9 5 3", "0 7 -1", "-5 2 9"]

matrix = []
rows = 0
columns = 0
while True:
    data = input()
    if data == "end":
        break
    else:
        row = [int(i) for i in data.split()]
        matrix.append(row)
        rows += 1
        columns = max(columns, len(row))

# 1
result = [[0] * columns for row in range(rows)]
for i in range(rows):
    for j in range(columns):
        result[i][j] = matrix[i-1][j] + matrix[(i+1) % rows][j] + matrix[i][j-1] + matrix[i][(j+1) % columns]

for row in result:
    print(*row)

# 2
[([print(matrix[i - 1][j] + matrix[i][j - 1] + matrix[i][(j + 1) % columns] + matrix[(i + 1) % rows][j], end=' ')
   for j in range(columns)], print()) for i in range(rows)]
