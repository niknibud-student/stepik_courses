def build_query_string(params):
    return '&'.join(sorted([f'{key}={val}' for key, val in params.items()]))

print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
