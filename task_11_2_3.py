balls = {
    'AEILNORSTU': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
}

word = input()
score = 0
for x in word:
    for letters in balls:
        if x in letters:
            score += balls[letters]
print(score)

print(sum([balls[letters] for x in word for letters in balls if x in letters]))


# d = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }

# print(sum([k for i in input() for k, v in d.items() if i in v]))
