# https://stepik.org/lesson/3368/step/10?unit=951

str = "1 3 5 6 10"  # input()
list = [int(i) for i in str.split()]
lenght = len(list)

if lenght == 1:
    print(list[0])
else:
    new_list = []
    for i in range(lenght):
        if i == 0:
            new_list.append(list[1] + list[-1])
        elif i == lenght - 1:
            new_list.append(list[0] + list[-2])
        else:
            new_list.append(list[i - 1] + list[i + 1])
    for i in new_list:
        print(i, end=" ")

    print()
    print(*new_list)    # !!! RTFM

    # !!! https://stepik.org/lesson/3368/step/10?discussion=346150&thread=solutions&unit=951
    for i in range(lenght):
        print(list[i - 1] + list[i + 1 - lenght], end=" ")
