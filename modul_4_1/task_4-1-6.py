import math as m

a, b = [int(x) for x in input().split()]

f = m.ceil((m.factorial(m.floor(b / a)) + a ** (b * m.pi)) / (m.log2(a) * m.sqrt(a / b) * m.cos(b + m.exp(a))))

print(f)