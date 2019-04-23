# python 3.7
# https://stepik.org/lesson/5047/step/4?unit=1086

room_type = input("треугольник / прямоугольник / круг ")

if room_type == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) * 0.5
    s2 = p * (p - a) * (p - b) * (p - c)
    print(s2 ** 0.5)

elif room_type == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a * b)

elif room_type == "круг":
    r = float(input())
    print(r ** 2 * 3.14)

else:
    print("Неопределен тип")
