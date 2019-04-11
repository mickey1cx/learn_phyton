# https://stepik.org/lesson/3369/step/4?unit=952


def print_minefield(minefield):
    for row in minefield:
        print(*row)


rows, columns, mines = 5, 4, 4  # int(input()), int(input()), int(input())
mines = [[1, 1], [2, 2], [3, 2], [4, 4]]
field = [[0 for j in range(columns)] for i in range(rows)]

for mine in mines:
    field[mine[0] - 1][mine[1] - 1] = "*"

print_minefield(field)
