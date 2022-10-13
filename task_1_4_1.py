def create(ns, prnt):
    scope[ns] = {'parent' : prnt, 'vars': set()}

def add(ns, var):
    scope[ns]['vars'].add(var)
    
def get(ns, var):
    if var in scope[ns]['vars']:
        return ns
    elif ns == 'global' and var not in scope[ns]['vars']:
        return None
    else:
        return get(scope[ns]['parent'], var)

n = int(input())

scope = {
    'global' : {
        'vars' : set()
        }
    }
a = []
for i in range(n):
    cmd, ns, var = input().split()
    if cmd == 'add':
        add(ns, var)        
    if cmd == 'create':
        create(ns,var)
    if cmd == 'get':
        a.append(get(ns, var))

print('\n'.join([str(i) for i in a]))