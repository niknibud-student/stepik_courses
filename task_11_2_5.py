def merge(values):      # values - это список словарей
    res = {}
    for dct in values:
        for key, val in dct.items():
            res.setdefault(key, set()).add(val)
            # res[key] = res.get(key, set()) | {value}
    return res


result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(result)

result = merge([{}, {}, {}])
print(result)
# result = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
