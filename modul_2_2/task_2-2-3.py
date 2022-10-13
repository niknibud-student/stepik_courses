time, border = map(int, input().split())
print(len([[2*x for x in [int(x) for x in input().split(', ')] if 2*x <= border] for i in range(time)]))