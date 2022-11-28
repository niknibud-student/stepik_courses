d = {}
for _ in range(int(input())):
    phone, name = input().lower().split()
    d.setdefault(name, []).append(phone)

for _ in range(int(input())):
    print(*d.get(input().lower(), ['Не найден']))
