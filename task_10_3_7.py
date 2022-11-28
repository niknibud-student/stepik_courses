s = input().split()

st = {}

for sym in s:
    st[sym] = st.get(sym, -1) + 1
    if st[sym] == 0:
        print(sym, end=' ')
    else:
        print(f'{sym}_{st[sym]}', end=' ')
