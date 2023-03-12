def only_one_positive(*args):
    cnt_pos = 0
    print(args)
    for x in args:
        if x > 0:
            cnt_pos += 1
    if cnt_pos == 1:
        return True
    return False

print(only_one_positive(1))
print(only_one_positive(1, 2))
print(only_one_positive(-1, 0, -3, 5, -3))
print(only_one_positive())

def print_goods(*args):
    lst = []
    for x in args:
        if type(x) == str and len(x) > 0:
            lst.append(x)
    if lst:
        for i, x in enumerate(lst, 1):
            print(f'{i}. {x}')
    else:
        print('Нет товаров')

print_goods('apple', 'banana', 'orange')
print_goods(1, True, 'Грушечка', '', 'Pineapple') 
print_goods([], {}, 1, 2) 

def info_kwargs(**kwargs):
            
    print(f"age = {kwargs['age']}")
    print(f"first_name = {kwargs['first_name']}")
    print(f"last_name = {kwargs['last_name']}")

info_kwargs(first_name="John", last_name="Doe", age=33)