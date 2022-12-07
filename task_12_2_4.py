import random as rnd

tickets = set()

while len(tickets) < 100:
    tickets.add(rnd.randint(1000000, 9999999))

print(*tickets, len(tickets), sep='\n')
