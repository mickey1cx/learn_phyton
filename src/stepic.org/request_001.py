# https://stepik.org/lesson/3378/step/2?unit=961

import requests as rq

r = rq.get('https://stepic.org/media/attachments/course67/3.6.2/273.txt')
data_file = r.text  # .strip()
l = data_file.splitlines()
print(len(l))
