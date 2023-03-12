def shift_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    num_letter = ord(letter) + shift
    print(num_letter)
    return chr(num_letter)

print(shift_letter('b', 2))
print(shift_letter('d', 1))
print(shift_letter('z', 1))
print(shift_letter('d', -2))
print(shift_letter('d', 26))
print(shift_letter('b', -3))