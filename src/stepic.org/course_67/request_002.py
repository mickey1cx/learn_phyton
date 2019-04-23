# https://stepik.org/lesson/3378/step/3?unit=961

import requests as rq
path = "https://stepic.org/media/attachments/course67/3.6.3/"
file_name = "699991.txt"

while True:
    url = path + file_name
    file = rq.get(url)
    file_text = file.text.strip()
    lines = file_text.splitlines()
    word = lines[0].split()[0]
    if word == "We":    # file_text.startswith('We')
        print(file_text)
        break
    else:
        file_name = word
        print(file_name)
