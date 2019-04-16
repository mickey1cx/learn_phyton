# https://stepik.org/lesson/3363/step/2?unit=1135

data_file = open("files/out.txt", "w")

numbers = [str(i) for i in range(10)]

with open('files/dataset.txt') as data_set:
    for str_line in data_set:
        str_line.strip()

        result = ""
        while len(str_line) > 0:
            print(str_line, len(str_line))
            symbol = str_line[0]
            num = ""
            ind = 1
            while ind < len(str_line) and str_line[ind] in numbers:
                num += str_line[ind]
                ind += 1
            result += symbol * int(num)
            str_line = str_line.split(num, 1)[1].strip()

        data_file.write(result)
    data_file.close()
