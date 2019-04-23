# https://stepik.org/lesson/3369/step/9?unit=952

num_str = "5 8 2 7 8 8 2 4"  # input()
num_list = [int(i) for i in num_str.split()]
i = 8  # int(input())
counter_list = []

counter = 0
for element in num_list:
    if element == i:
        counter_list.append(counter)
    counter += 1

if len(counter_list) > 0:
    print(*counter_list)
else:
    print("Отсутствует")

# 2

if i not in num_list:
    print("Отсутствует")
else:
    for index in range(len(num_list)):   # enumerate
        if num_list[index] == i:
            print(index, end=" ")

print()
# 3

if i not in num_list:
    print("Отсутствует")
else:
    for index, element in enumerate(num_list):
        if element == i:
            print(index, end=" ")
