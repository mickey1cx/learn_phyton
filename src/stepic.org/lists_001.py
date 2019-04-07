# https://stepik.org/lesson/3368/step/10?unit=951

str = input()
list = [int(i) for i in str.split()]
lenght = len(list)

if lenght == 1:
    print(list[0])
else:
    new_list = []
    for i in range(0, lenght):
        if i == 0:
            new_list.append(list[1] + list[-1])
        elif i == lenght - 1:
            new_list.append(list[0] + list[-2])
        else:
            new_list.append(list[i - 1] + list[i + 1])
    for i in new_list:
        print(i, end=" ")
