# python 3.7
# https://stepik.org/lesson/5047/step/7?unit=1086

ticket = input()

a = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
b = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

if a == b:
    print("Счастливый")
else:
    print("Обычный")

