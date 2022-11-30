code = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}

rnk = ''
for x in input():
    rnk += code[x]

print(rnk)

