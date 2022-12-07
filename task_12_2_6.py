import random as rnd

lst = rnd.sample(range(1, 76), 25)
lst[12] = 0

for i in range(5, 26, 5):
    print(*[str(x).ljust(3) for x in lst[i-5:i]])

