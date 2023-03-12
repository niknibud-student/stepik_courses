MIN_DRIVING_AGE = 18

def allowed_driving(name: str, age: int) -> None:
    if age >= MIN_DRIVING_AGE:
        print(f'{name} можеть водить')
    else:
        print(f'{name} еще рано садиться за руль')

# allowed_driving('tim', 17) # выведет "tim еще рано садиться за руль"
# allowed_driving('bob', 18) # выведет "bob может водить"

def get_word_indices(strings: list[str]) -> dict:
    dct = {}
    for i, line in enumerate(strings):
        for word in line.lower().split():
            if word in dct:
                dct[word].append(i)
            else:
                dct[word] = [i]
    return dct

print(get_word_indices(['This is a string',
                         'test String',
                         'test',
                         'string']))