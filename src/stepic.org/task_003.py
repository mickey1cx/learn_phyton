# https://stepik.org/lesson/3380/step/3?unit=963

count_samples = 3
samples = ["a", "bb", "ccc"]
# samples = []
# for i in range(count_samples):
#     samples.append(input().lower())

count_lines = 2
lines = ["a bb aab aba ccc", "c bb aaa"]
# lines = []
# for i in range(count_lines):
#     lines.append(input().lower())

words = {}

for line in lines:
    line_words = line.split()
    for word in line_words:
        if word not in samples:
            words.setdefault(word)

for key in words.keys():
    print(key)

# 2 modify https://stepik.org/lesson/3380/step/3?discussion=973134&thread=solutions&unit=963
samples_dict = {x for i, x in enumerate(samples)}
words_dic = {k for i in range(count_lines) for k in lines[i].split()}
print('\n'.join(words_dic - samples_dict))
