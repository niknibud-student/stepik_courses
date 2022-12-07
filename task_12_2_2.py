def generate_index():
    import string as s
    import random as rnd

    LETTERS = s.ascii_uppercase

    return f'{"".join(rnd.sample(LETTERS, 2))}{rnd.randint(0, 99)}_{rnd.randint(0, 99)}{"".join(rnd.sample(LETTERS, 2))}'

print(generate_index())
