# https://stepik.org/lesson/3368/step/11?unit=951

num_str = "4 8 0 3 4 2 0 3" # input()
num_list = [int(i) for i in num_str.split()]
num_list.sort()

if len(num_list) > 1:
    counter = 0
    current_number = num_list[0]
    num_list.pop(0)
    num_list.append(-1)
    for i in num_list:
        if current_number == i:
            counter += 1
        else:
            if counter > 0:
                print(current_number, end=" ")
            current_number = i
            counter = 0

# 2

num_list = [int(i) for i in num_str.split()]
num_list.sort()

print()
for i in set(num_list):
    if num_list.count(i) > 1:
        print(i, end=" ")

# 3
print()
print(*(i for i in set(num_list) if num_list.count(i) > 1))
