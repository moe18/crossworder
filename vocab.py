from nltk.corpus import words
from image_getter import get_puzzel
import random

import numpy as np



wordlist = words.words()

puzzel = get_puzzel()

across = []
down = []
for row in puzzel:
    row = row.astype('str')
    count = 0
    count2 = 0
    print(row)
    for i in row:
        count2 += 1
        if i=='1.0':
            count+=1
        else:
            if count > 0:
                words = [word for word in wordlist if len(word) == count]
                secure_random = random.SystemRandom()
                word = secure_random.choice(words)
                across.append(word)
                across.append('0')
                print(word)
            else:
                across.append('0')

            count = 0
        print(count2,'heyy')
        if count2 == len(row):
            if count > 0:
                words = [word for word in wordlist if len(word) == count]
                secure_random = random.SystemRandom()
                word = secure_random.choice(words)
                across.append(word)
                print(word)



    count2 = 0



across2 = []
for i in across:
    across2.extend(list(i))

print(len(across2))
x = np.reshape(across2, (15, 15))
print(x)