n = int(input())
for i in range(n):
    x = input()
    y = abs(int(''.join(list(x).sort(reverse=True))))
    print(y)