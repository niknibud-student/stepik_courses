keys = {
    '.,?!:': '1',
    'ABC': '2',
    'DEF': '3',
    'GHI': '4',
    'JKL': '5',
    'MNO': '6',
    'PQRS': '7',
    'TUV': '8',
    'WXYZ': '9',
    ' ': '0'
}

line = input().upper()
code = ''
for sym in line:
    for key in keys:
        if sym in key:
            idx = key.index(sym) + 1
            code += keys[key] * idx
print(code)
