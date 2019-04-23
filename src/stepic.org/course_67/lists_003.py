# https://stepik.org/lesson/3369/step/7?unit=952

numbers = [1, -3, 5, -6, -10, 13, 4, -8]

summ = 0
summ_2 = 0
for i in numbers:
    summ += i
    summ_2 += i**2
    if summ == 0:
        break

print(summ_2)
