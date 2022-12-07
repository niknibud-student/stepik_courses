import random

n = int(input())    # количество попыток

for _ in range(n):
    print(random.choice([1, 2, 3, 4, 5, 6]))

for _ in range(n):
    print(random.randint(1, 6))
