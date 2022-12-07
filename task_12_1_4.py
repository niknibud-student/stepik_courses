# 1
import random

ticket_number = []

while len(ticket_number) < 7:
    num = random.randint(1, 49)
    if num in ticket_number:
        continue
    ticket_number.append(num)

print(*sorted(ticket_number))

# 2
s = set()
while len(s) < 7:
    s.add(random.randint(1, 49))

print(*sorted(s))

#3
import random as rnd
print(*sorted(rnd.sample(range(1, 50), 7)))

#4
import random
s = list(range(1, 50))
random.shuffle(s)
print(*sorted(s[:7]))
