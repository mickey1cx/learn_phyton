# https://stepik.org/lesson/3372/step/9?unit=955


def modify_list(l):
    new_l = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            new_l.append(l[i] // 2)
    l.clear()
    for i in new_l:  # l.extend(new_l); l += new_l
        l.append(i)


# https://stepik.org/lesson/3372/step/9?discussion=940546&thread=solutions&unit=955
def modify_list2(l):
    l[:] = [d // 2 for d in l if not d % 2]


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)  # [1, 2, 3]
modify_list(lst)
print(lst)  # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)  # [5, 4]
