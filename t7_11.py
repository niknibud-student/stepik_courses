taxi_drivers = {}
while True:
    data = input()
    if data == 'конец':
        break
    name, rank = data.split(', ')
    if name in taxi_drivers:
        taxi_drivers[name][0] += int(rank)
        taxi_drivers[name][1] += 1
    else:
        taxi_drivers[name] = [rank, 1]
for name, avg in sorted(taxi_drivers.items(), key=lambda x: x[1][0]/x[1][1]):
    print(name, round(avg[0]/avg[1], 1))
    