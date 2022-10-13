n = int(input())
mx = ' '
for i in range(n):
    x = input()
    if max(x) > max(mx) and len(x) >= len(mx):
        mx = x
print(mx)