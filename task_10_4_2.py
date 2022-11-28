fline = list(input())
sline = list(input())

fdict = {s: fline.count(s) for s in set(fline)}
sdict = {s: sline.count(s) for s in set(sline)}

print('YES' if fdict == sdict else 'NO')
