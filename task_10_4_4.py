n = int(input())
syns = {}

for _ in range(n):
    word1, word2 = input().split()
    syns[word1] = word2
    syns[word2] = word1

print(syns[input()])

