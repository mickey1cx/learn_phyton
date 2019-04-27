# https://stepik.org/lesson/22774/step/2?adaptive=true&unit=5345
# counting, format, number-formatting

scores = 'F B A A B C A D'  # input()
score_list = scores.split()
count_A = score_list.count('A')
print("{:.2f}".format(count_A / len(score_list), 2))

# 2

import collections

c = collections.Counter(score_list)
print("%.2f" % (c['A'] / len(score_list)))
