import re


def get_advice_books(request, library, users):
    advice_books = []
    name = re.search(r'\((\w*)\)', request)
    user_books = users[name[1]]
    print(f'{name[1]}: {", ".join(user_books)}')
    
    for user_book in user_books:
        for books in library.values():
            if user_book in books:
                if user_book in advice_books:
                    advice_books.remove(user_book)
                else:
                    books.remove(user_book)
                    advice_books.extend(books)
    return advice_books

def get_advice_books_v2(request, library, users):
    advice_books = {}
    name = re.search(r'\((\w*)\)', request)
    user_books = users[name[1]]
    print(f'{name[1]}: {", ".join(user_books)}')
    
    favorite_genres = {}
    for user_book in user_books:
        print(user_books)
        for genre, books in library.items():
            if user_book in books:
                print(f'{user_book}: {user_book in books}')
                if genre not in favorite_genres:
                    # print(f'{genre}: {genre not in favorite_genres}')
                    favorite_genres[genre] = 1
                    books.remove(user_book)
                    advice_books[genre] = books
                else:
                    favorite_genres[genre] += 1
                    advice_books[genre].remove(user_book)
            else:
                continue
    print(favorite_genres)
    print(advice_books)
    max_num = max(favorite_genres.values())
    favorite_genres = [k for k, v in favorite_genres.items() if v == max_num]
    advice_books = [v for k, v in advice_books.items() if k in favorite_genres]
    return advice_books[0]