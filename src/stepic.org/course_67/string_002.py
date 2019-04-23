# https://stepik.org/lesson/3367/step/7?unit=950

dna = input()   # "aaaabbсaa"
code = ""
last_code = ""
counter = 0

for i in dna:
    if last_code != i:
        if counter > 0:
            code = code + last_code + str(counter)
        last_code = i
        counter = 1
    else:
        counter += 1

if counter > 0:
    code = code + last_code + str(counter)

print(code)
