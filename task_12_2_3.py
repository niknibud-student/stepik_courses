import random as rnd

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

for i in range(len(matrix)):
    rnd.shuffle(matrix[i])

print(matrix)
