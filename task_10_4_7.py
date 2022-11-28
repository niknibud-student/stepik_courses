enc_line = input()

enc_dict = {sym: enc_line.count(sym) for sym in set(enc_line)}

dec_dict = {}

for _ in range(int(input())):
    sym, cnt = input().split(': ')
    dec_dict[int(cnt)] = sym

for x in enc_line:
    print(dec_dict[enc_dict[x]], end='')
