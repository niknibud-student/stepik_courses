n = int(input())

shop = {}

for _ in range(n):
    customer, goods, cnt = input().split()
    shop.setdefault(customer, {})
    shop[customer].setdefault(goods, 0)
    shop[customer][goods] = shop[customer].get(goods, 0) + int(cnt)

# shop = {'Вячеслав': {'Ручка': 30, 'Линейка': 4}, 'Филипп': {'Ручка': 1, 'Циркуль': 1}, 'Виктория': {'Перо': 3, 'Тетрадь': 7}}

for customer, goods in sorted(shop.items(), key=lambda x: x):
    print(f'{customer}:')
    for thing, cnt in sorted(goods.items(), key=lambda x: x):
        print(thing, cnt)
