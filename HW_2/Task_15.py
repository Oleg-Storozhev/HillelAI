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
