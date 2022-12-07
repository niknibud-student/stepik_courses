import random as rnd
n = int(input())
students = {}

for _ in range(n):
    students.setdefault(input(), '')

friends = list(students)

rnd.shuffle(friends)
k = len(friends)

for i in range(k):
    students[friends[i]] = friends[i+1] if i+1 < k else friends[0]
for s, f in students.items():
    print(f'{s} - {f}')

