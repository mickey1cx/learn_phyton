# python 3.7
# https://stepik.org/lesson/5047/step/3?unit=1086

print("input numbers: ")
a = float(input())
b = float(input())
action = input("+, -, /, *, mod, pow, div : ")

if action == "+":
    print(a + b)
elif action == "-":
    print(a - b)
elif action == "*":
    print(a * b)
elif action == "/":
    if b == 0:
        print("Деление на 0!")
    else:
        print(a / b)
elif action == "mod":
    if b == 0:
        print("Деление на 0!")
    else:
        print(a % b)
elif action == "pow":
    print(a ** b)
elif action == "div":
    if b == 0:
        print("Деление на 0!")
    else:
        print(a // b)
else:
    print("Неопределена операция")
