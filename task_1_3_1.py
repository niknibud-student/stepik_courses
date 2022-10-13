def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        return (x + 5 - x % 5)

print(closest_mod_5(10))
print(closest_mod_5(0))
print(closest_mod_5(13))
print(closest_mod_5(101010111111))