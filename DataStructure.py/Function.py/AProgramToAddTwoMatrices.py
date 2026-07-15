X = [[2, 5, 4],
     [1, 3, 9],
     [7, 6, 2]]
Y = [[1, 8, 5],
     [7, 3, 6],
     [4, 0, 9]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)