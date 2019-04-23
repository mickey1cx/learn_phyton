# https://stepik.org/lesson/21208/step/2?adaptive=true&thread=solutions&unit=5094
def my_func(x):
    if x <= -2:
        result = 1 - (x + 2) ** 2
    elif x > 2:
        result = (x - 2) ** 2 + 1
    else:
        result = -x / 2
    return result


print(my_func(4.5))
print(my_func(-4.5))
print(my_func(1.0))
