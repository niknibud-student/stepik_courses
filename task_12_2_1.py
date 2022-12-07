def generate_ip():
    import random as rnd
    return '{}.{}.{}.{}'.format(*[rnd.randint(0, 255) for _ in range(4)])

print(generate_ip())

from random import randrange as r

def generate_ip2():
    return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'

def generate_ip3():
    import random
    return '.'.join(str(i) for i in random.sample(range(256), 4))
