fsent = input().lower()
ssent = input().lower()

fdict = {s: fsent.count(s) for s in set(fsent) if s not in '.,!?:;- '}
sdict = {s: ssent.count(s) for s in set(ssent) if s not in '.,!?:;- '}

print('YES' if fdict == sdict else 'NO')
