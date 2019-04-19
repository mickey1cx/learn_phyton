# https://stepik.org/lesson/3380/step/1?unit=963


def result(command_data, res1, res2):
    command_data[0] += 1
    if res1 > res2:
        command_data[1] += 1
        command_data[4] += 3
    elif res1 < res2:
        command_data[3] += 1
    else:
        command_data[2] += 1
        command_data[4] += 1


count = 3   # int(input())
commands = {}

list_str = ["Зенит;3;Спартак;1", "Спартак;1;ЦСКА;1", "ЦСКА;0;Зенит;2"]

for i in range(count):
#    data = input().split(";")
    data = list_str[i].split(";")
    command1 = commands.setdefault(data[0], [0]*5)
    command2 = commands.setdefault(data[2], [0]*5)
    result(command1, data[1], data[3])
    result(command2, data[3], data[1])

for i, value in commands.items():
    print(i + ":", end="")
    print(*value)
