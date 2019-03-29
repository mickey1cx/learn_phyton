# python 3.7
# https://stepik.org/lesson/3364/step/12?unit=947

a = int(input())
b = int(input())
d = max(a, b)

while d % a != 0 or d % b != 0:
    d += 1

print(d)
