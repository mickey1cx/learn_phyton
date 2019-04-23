# https://stepik.org/lesson/3380/step/2?unit=963


def code_string(data, dict):
    result = ""
    for key in data:
        result += dict[key]
    return result


#strings, keys, data, code = input(), input(), input(), input()
strings, keys, data, code = "abcd", "*d%#", "abacabadaba", "#*%*d*%"
code_data = {}
decode_data = {}
for i in range(len(strings)):
    code_data[strings[i]] = keys[i]
    decode_data[keys[i]] = strings[i]

print(code_string(data, code_data))
print(code_string(code, decode_data))

# 2 https://stepik.org/lesson/3380/step/2?discussion=961286&thread=solutions&unit=963
code_table = str.maketrans(strings, keys)
decode_table = str.maketrans(keys, strings)
print(data.translate(code_table))
print(code.translate(decode_table))
