ans = 0
objs = set()
for obj in objects: # доступная переменная objects
    objs.add(id(obj))

ans = len(objs)

print(ans)