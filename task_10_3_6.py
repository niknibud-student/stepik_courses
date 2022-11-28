s = [word.strip('.,!?:;-') for word in input().lower().split()]

words = {}

for word in s:
    words[word] = words.get(word, 0) + 1

words = {word: s.count(word) for word in set(s)}

print(min(words, key=lambda x: (words[x], x)))
