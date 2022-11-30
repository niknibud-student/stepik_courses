dct = {
    'write': 'W',
    'read': 'R',
    'execute': 'X'
}

n = int(input())
filesys = {}
for _ in range(n):
    file, *rights = input().split()
    filesys[file] = rights

n = int(input())
for x in range(n):
    act, file = input().split()
    if dct[act] in filesys[file]:
        print('OK')
    else:
        print('Access denied')


