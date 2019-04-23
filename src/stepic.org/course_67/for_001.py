# https://stepik.org/lesson/3366/step/3?unit=949

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print("", end="")
for j in range(c, d + 1):
    print("\t" + str(j), end="")
print()

for i in range(a, b + 1):
    print(str(i), end="")
    for j in range(c, d + 1):
        print("\t" + str(i * j), end="")
    print()
