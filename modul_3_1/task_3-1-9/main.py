import sys
f = open('input2.txt', 'r')
sys.stdin = f

from funcs import get_advice_books_v2


data = [x.strip() for x in input().split(',')]
library = {}
for item in data:
    book = [x.strip(' ()') for x in item.split('"')]
    if book[-1] in library:
        library[book[-1]].append(book[1])
    else:
        library[book[-1]] = [book[1]]

#for item, val in library.items():
#    print(f'{item}: {val}')

users = {}
request = input()
while request != '.':
    if 'Посоветуй' in request:
        advice_books = get_advice_books_v2(request, library, users)
        if advice_books:
            print(', '.join([f'"{x}"' for x in advice_books]))
        else:
            print('Список пуст')

    else:
        user = request.split(' "')
        if user[0] in users:
            users[user[0]].append(user[1][:-1])
        else:
            users[user[0]] = [user[1][:-1]]
    request = input()

f.close()
