def dbl_linear(n):
    u = [1]
    i = j = 0
    while len(u) <= n:
        x_1 = 2 * u[i] + 1
        x_2 = 3 * u[j] + 1
        if x_1 < x_2:
            u.append(x_1)
            i += 1
        elif x_1 > x_2:
            u.append(x_2)
            j += 1
        else:
            u.append(x_1)
            i += 1
            j += 1
    return u[n]


assert dbl_linear(10) == 22
assert dbl_linear(20) == 57
assert dbl_linear(30) == 91
assert dbl_linear(50) == 175
