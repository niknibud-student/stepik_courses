def right_password(password: str) -> bool:
    import string as s
    pwd = set(password)
    if set(s.ascii_lowercase) & pwd and set(s.ascii_uppercase) & pwd and set(s.digits) & pwd:
        return True
    return False

def generate_password(length: int) -> str:
    """возвращает случайный пароль длиной length символов"""
    import string as s
    import random as rnd
    LETTERS = ''.join((set(s.ascii_letters) | set(s.digits)) - set('lI1oO0'))
    return ''.join(rnd.sample(LETTERS, k=length))


def generate_passwords(count: int, length: int) -> list:
    """возвращает список, состоящий из count случайных паролей длиной length символов"""
    passwords = []
    while len(passwords) < count:
        password = generate_password(length)
        if right_password(password):
            passwords.append(password)
    return passwords

n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')


# import random, string

# def generate_password(length):
#     flag = False
#     while not flag:
#         t = set(random.sample(l, length))
#         if t & set(string.digits) and t & set(string.ascii_uppercase) and t & set(string.ascii_lowercase):
#             flag = True
#     return ''.join(t)

# def generate_passwords(count, length):
#     return [generate_password(length) for _ in range(count)]

# n, m = int(input()), int(input())
# l = ''.join((set(string.ascii_letters) | set(string.digits)) - set('lI1oO0'))
# print(*generate_passwords(n, m), sep='\n')
