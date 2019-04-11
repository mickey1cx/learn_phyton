# https://stepik.org/lesson/3369/step/4?unit=952


def print_minefield(minefield):
    for row in minefield:
        print(*row)


rows, columns, mines = 5, 4, 4  # int(input()), int(input()), int(input())
mines = [[1, 1], [2, 2], [3, 2], [4, 4]]
field = [[0 for j in range(columns)] for i in range(rows)]

for mine in mines:
    field[mine[0] - 1][mine[1] - 1] = "*"

for i in range(rows):
    imin = 0 if i == 0 else -1
    imax = 0 if i == rows - 1 else 1
    for j in range(columns):

        if field[i][j] == "*":
            continue

        jmin = 0 if j == 0 else -1
        jmax = 0 if j == columns - 1 else 1

        counter = 0
        for ii in range(imin, imax + 1):
            for jj in range(jmin, jmax + 1):
                if ii == 0 and jj == 0:
                    continue
                elif field[i + ii][j + jj] == "*":
                    counter += 1
        field[i][j] = counter if counter > 0 else "."

print_minefield(field)
