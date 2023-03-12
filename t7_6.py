def create_matrix(size: int=3, up_fill: int=0, down_fill: int=0) -> list:
    lst = [[0]*size for _ in range(size)]
    for i in range(size):
        lst[i][i] = i+1
    if up_fill != 0:
        for i in range(size):
            for j in range(i+1, size):
                lst[i][j] = up_fill
    if down_fill != 0:
        for i in range(size):
            for j in range(i):
                lst[i][j] = down_fill
    return lst

import pprint
# res = create_matrix()
# res = create_matrix(4)
# res = create_matrix(up_fill=7)
# res = create_matrix(up_fill=7, down_fill=9)
# res = create_matrix(size=4, up_fill=7, down_fill=9)
res = create_matrix(size=10, up_fill=17, down_fill=-1)
for x in res:
    print(x)