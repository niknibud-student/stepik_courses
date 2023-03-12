def get_domain_name(url):
    url = url.replace('https://', '')
    url = url.replace('http://', '')
    url = url.replace('www.', '')
    return url.split('.')[0]

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n

def factorial(n):
    import math
    return math.factorial(n)

def trailing_zeros(n):
    n = factorial(n)
    zero = 0
    for x in str(n)[::-1]:
        if x == '0':
            zero += 1
        else:
            return zero
            break

def count_AGTC(dna):
    return tuple(dna.count(x) for x in 'AGTC')


# print(get_domain_name("http://google.com"))
# print(get_domain_name("http://google.co.jp"))
# print(get_domain_name("www.xakep.ru"))
# print(get_domain_name("https://youtube.com"))
# print(get_domain_name("https://www.asos.com"))
# print(get_domain_name("http://www.lenovo.com"))

# print(trailing_zeros(6))
# print(trailing_zeros(10))
# print(trailing_zeros(20))

print(count_AGTC('AGGTC'))
print(count_AGTC('AAAATTT'))
print(count_AGTC('AGTTTTT'))
print(count_AGTC('CCT'))