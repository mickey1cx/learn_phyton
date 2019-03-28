# python 3.7
# https://stepik.org/lesson/5047/step/6?unit=1086


def string_count(count_number):

    c100 = (count_number // 100)
    count_number = count_number - c100 * 100

    c10 = (count_number // 10)
    count_number = count_number - c10 * 10

    if c10 != 1 and count_number == 1:
        string_counter = "программист"
    elif c10 != 1 and (count_number >= 2) and count_number <= 4:
        string_counter = "программиста"
    else:
        string_counter = "программистов"

    return string_counter


count = int(input())
print(str(count) + " " + string_count(count))

