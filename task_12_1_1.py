import random

n = int(input())    # количество попыток

for _ in range(n):
    coin = ['Орел', 'Решка']
    print(coin[random.randint(0, 1)])

for _ in range(n):
    print(random.choice(['Орел', 'Решка']))
