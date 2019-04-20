# https://stepik.org/lesson/3380/step/4?unit=963

direction = {"север": [0, 1], "юг": [0, -1], "восток": [1, 0], "запад": [-1, 0]}
position = [0, 0]
counter = int(input())
for i in range(counter):
    move = input().split()
    move_vector = direction[move[0]]
    move_length = int(move[1])
    position[0] += move_vector[0] * move_length
    position[1] += move_vector[1] * move_length

print(position)
