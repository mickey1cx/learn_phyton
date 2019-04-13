# https://stepik.org/lesson/3369/step/10?unit=952

string_list = ["9 5 3", "0 7 -1", "-5 2 9"]
matrix = []

columns = 3
rows = 3
result = [[0] * columns for row in range(rows)]

for element in string_list:
    matrix.append([int(i) for i in element.split()])

for i in range(columns):
    for j in range(rows):
        over_i = i + 1 if i + 1 < columns else 0
        over_j = j + 1 if j + 1 < rows else 0
        result[i][j] = matrix[i-1][j] + matrix[over_i][j] + matrix[i][j-1] + matrix[i][over_j]

print(*matrix)
print(*result)
