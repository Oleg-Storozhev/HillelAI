# Дано знак “+” або “*”, число N і N чисел.
# Вивести суму або добуток введених чисел залежно від заданого знаку.

def sum_or_mul(x, op):
    x = abs(int(x))
    if x == 0 or (not op == "*" and not op == "+"):
        return 0
    res = float(input("1: "))
    for i in range(x-1):
        if op == "*":
            res *= float(input(str(i+2)+": "))
        else:
            res += float(input(str(i+2)+": "))
    return res


a, b = input("Write a number and the operation: ").split()
print(sum_or_mul(a, b))
