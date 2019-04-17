# https://stepik.org/lesson/3363/step/3?unit=1135

words = {}
with open("files/dataset2.txt") as data_set:
    for line in data_set:
        data = line.strip().split()
        for word in data:
            key = word.lower()
            if key not in words:
                words[key] = 1
            else:
                words[key] += 1

sort_words = sorted(words, key=words.get, reverse=True)
# поиск ключей с одинаковым количеством
value = 0
keys = []
for key in sort_words:
    value = max(value, words[key])
    if value == words[key]:
        keys.append(key)
    else:
        break

keys.sort()
key = keys[0]
print(key, words[key])
