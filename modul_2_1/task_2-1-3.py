num = [int(x) for x in input().split(', ')]
min_x = min(num)
idx = 0
sum_idx = 0
for i in range(num.count(min_x)):
    idx = num.index(min_x, idx + 1)
    sum_idx += idx
print(sum_idx)