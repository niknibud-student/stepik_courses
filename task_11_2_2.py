words = 'прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон'.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1
    print(freq[word], end=' ')

# d = {}
# for s in input().split():
#     print(d.setdefault(s, 1), end=' ')
#     d[s] += 1
