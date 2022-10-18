# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import re

s = "автобус аэробус машина зимбабве самозабвенный главрыба Напишите программу, удаляющую из текста все слова, содержащие"
words = re.split('\W+', s)

ex = ["а", "б", "в"]

# for i in range(len(words)):
#     if words[i].find(ex[0]) != -1 and words[i].find(ex[1]) != -1 and words[i].find(ex[2]) != -1:
#         words[i] = None
for i in range(len(words)-1, -1, -1):
    print(i)
    if words[i].find(ex[0]) != -1 and words[i].find(ex[1]) != -1 and words[i].find(ex[2]) != -1:
        # print(words.pop(i))
        del words[i]
print(words)
