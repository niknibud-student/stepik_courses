from simplecrypt import encrypt, decrypt

pwds = []
with open('passwords.txt') as p:
    for line in p.readlines():
        pwds.append(line.rstrip())
print(pwds)
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
#print(encrypted)
for pwd in pwds:
    try:
        plaintext = decrypt(pwd, encrypted)
    except Exception: 
        continue
    print(plaintext)