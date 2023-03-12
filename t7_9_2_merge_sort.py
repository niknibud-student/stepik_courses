def merge_two_list(a: list, b: list) -> list:
    lst = []
    l = r = 0
    l_len, r_len = len(a), len(b)

    for _ in range(l_len + r_len):
        if l < l_len and r < r_len:
            if a[l] <= b[r]:
                lst.append(a[l])
                l += 1
            else:
                lst.append(b[r])
                r += 1
        elif l == l_len:
            lst.append(b[r])
            r += 1
        elif r == r_len:
            lst.append(a[l])
            l += 1
    return lst


def merge_sort(s: list) -> list:
    if len(s) <= 1:
        return s
    
    mid = len(s) // 2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])
    return merge_two_list(left, right)

# assert merge_sort([11, 15, 19, 20, 20, 6, 4, 16, 8]) == [4, 6, 8, 11, 15, 16, 19, 20, 20], "Функция merge_sort возвращает неправильный результат"

print(merge_sort([11, 15, 19, 20, 20, 6, 4, 16, 8]))
