lst = [int(x) for x in input().split()]
count = {x: 0 for x in set(lst)}
for i in lst:
    count[i] += 1
print(*[j * count[j] for j in range(min(lst), max(lst)+1) if j in count.keys()])