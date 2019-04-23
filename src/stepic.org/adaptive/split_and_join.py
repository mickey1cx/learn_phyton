# https://stepik.org/lesson/22775/step/2?adaptive=true&unit=5348
file_name = input()  # 'string     with        multi spaces', 'my file name.txt', 'single'
list_name = file_name.split()
print("_".join(list_name))
