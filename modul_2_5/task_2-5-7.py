import itertools
def subs(l):
    res = []
    for i in range(1, len(l) + 1):
        for combo in itertools.combinations(l, i):
            res.append(set(combo))
    return res

print({}, *subs([1, 3, 2, 4]), sep=', ')