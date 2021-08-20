# Дано число N - кількість чисел до вводу та самі числа.
# Вивести максимум серед введених чисел.

def max(x):
    if x == 0:
        return 0
    max = float(input())
    for i in range(abs(x)-1):
        n = float(input())
        if max < n:
            max = n
    return max


print(max(int(input("How many numbers will you write? "))))
