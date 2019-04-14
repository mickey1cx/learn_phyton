# https://ru.stackoverflow.com/questions/969622

neps = [
    "Test1 Test2 Test1 Test3"]

dict = {}
for i in range(len(neps)):
    slova = neps[i].split(" ")
    for w in range(len(slova)):
        # if slova[w] in dict == False:
        # ошибка построения логического выражения
        # необходимо заключить проверку вхождения в скобки
        # (slova[w] in dict) == False, или :
        if not slova[w] in dict:
            dict[slova[w]] = 1
        else:
            dict[slova[w]] += 1

# some magic

from itertools import chain
from collections import Counter
frequencies = Counter(chain.from_iterable(i.split() for i in neps))
