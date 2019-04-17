# https://stepik.org/lesson/3363/step/4?unit=1135

avg = [0]*3
counter = 0
with open("files/data3.txt") as data_set:
    for line in data_set:
        counter += 1
        data = line.strip().split(";")
        print((int(data[1]) + int(data[2]) + int(data[3])) / 3)
        avg[0] += int(data[1])
        avg[1] += int(data[2])
        avg[2] += int(data[3])
print(avg[0] / counter, avg[1] / counter, avg[2] / counter)
