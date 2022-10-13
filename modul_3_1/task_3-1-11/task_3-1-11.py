goods = []
start_price = 0
bidders = []

rates = {}

lines = []
with open('task3_1st11.txt', encoding = "utf-8-sig") as f:
    while True:
        s = f.readline()[:-1]        
        if not s:
            break
        lines.append(s)
    
goods = lines[0].split(', ')
start_price = int(lines[1])
bidders = lines[2].split(', ')

for line in lines[3:]:
    rate = line.split()
    if rate[0] in bidders:
        if ' '.join(rate[1:-1]) in rates:
           rates[' '.join(rate[1:-1])].append([rate[0], int(rate[-1])])
        else:
            rates[' '.join(rate[1:-1])] = [[rate[0], int(rate[-1])]]
    else:
        continue

for item in goods:
    if item in rates:
        if len(rates[item]) > 1:
            rates[item].sort(reverse=True, key=lambda x: x[1])
        if rates[item][0][1] >= start_price:
            print(item, rates[item][0][0], rates[item][0][1])
        
    if item not in rates or rates[item][0][1] < start_price:
        print(item, 'Предложений не было')