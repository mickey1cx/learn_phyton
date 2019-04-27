# https://stepik.org/lesson/23897/step/1?adaptive=true&unit=6423

start, end = 0x1F600, 0x1F64F
offset = int(input())
uni_string = input()    # '😀🙏😇'

result = ''
for char in uni_string:
    result += chr(start + (ord(char) - start + offset) % (end - start + 1))

print('Result: "' + result + '"')
