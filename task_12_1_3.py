import random

length = int(input())    # длина пароля

print(*random.choices([chr(code) for code in range(65, 91)] + [chr(code) for code in range(97, 123)], k=length), sep='')

from random import randint as R

for _ in range(int(input())):
    print([chr(R(65, 90)), chr(R(97, 122))][R(0, 1)], end = '')
