import math
n = int(input())
a = int(input())
for i in range(n - 1):
    a = math.gcd(a, int(input()))
print(a)