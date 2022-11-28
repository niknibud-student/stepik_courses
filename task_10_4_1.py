n = int(input())
dict_prog = {}

for _ in range(n):
    term, desc = input().split()
    dict_prog[term] = desc

x = int(input())

for _ in range(x):
    print(dict_prog.get(input(), 'Не найдено')
