# https://stepik.org/lesson/21209/step/2?adaptive=true&unit=5095
def modify_list(l):
    new_l = [int(x/2) for x in l if x % 2 == 0]
    l.clear()
    l.extend(new_l)


def modify_list_2(numbers):
    numbers[:] = [i//2 for i in numbers if i % 2 == 0]


lst = [1, 2, 3, 4, 5, 6]
print(modify_list_2(lst))  # None
print(lst)               # [1, 2, 3]
modify_list_2(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list_2(lst)
print(lst)
