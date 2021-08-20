def matrix_mul(a, b):
    answ = []
    for i in range(len(a)):
        row = []
        for j in range(len(a)):
            x = 0
            for k in range(len(a)):
                x += a[i][k]*b[k][j]
            row.append(x)
        answ.append(row)
    return answ


assert matrix_mul([[1, 2], [3, 2]], [[3, 2], [1, 1]]) == [[5, 4], [11, 8]]
assert matrix_mul([[9, 7], [0, 1]], [[1, 1], [4, 12]]) == [[37, 93], [4, 12]]
assert matrix_mul([[1, 2, 3], [3, 2, 1], [2, 1, 3]], [[4, 5, 6], [6, 5, 4], [4, 6, 5]]) == [[28, 33, 29], [28, 31, 31], [26, 33, 31]]
