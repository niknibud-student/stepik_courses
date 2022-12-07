import random as rnd

word = list(input())

rnd.shuffle(word)
print(''.join(word))
