# https://stepik.org/lesson/3380/step/5?unit=963

# lines = [
# '6	Вяххи	159'.split('\t'),
# '11	Федотов	172'.split('\t'),
# '7	Бондарев	158'.split('\t'),
# '6	Чайкина	153'.split('\t')
# ]

average = {i + 1: [0, 0] for i in range(11)}

with open('files/average.txt') as f:
    for line in f:
        i = line.split('\t')
        key = int(i[0])
        average[key][0] += int(i[2])
        average[key][1] += 1

for key, value in average.items():
    if value[0] == 0:
        print(key, '-')
    else:
        print(key, value[0] / value[1])
