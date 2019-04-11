# https://stepik.org/lesson/3369/step/8?unit=952

i = int(input())
counter = 0
current_number = 0

while counter != i:
    current_number += 1
    for j in range(current_number):
        print(current_number, end=" ")
        counter += 1
        if counter == i:
            break
