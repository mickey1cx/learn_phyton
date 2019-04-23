# https://stepik.org/lesson/3372/step/8?unit=955


def func(param_x):
    if param_x <= -2:
        return 1 - (param_x + 2) ** 2
    elif param_x > 2:
        return 1 + (param_x - 2) ** 2
    else:
        return -param_x / 2


x = float(input())
print(func(x))
