# Дано число N.
# Вивести послідовність чисел Фібоначчі, що менші від N.

fib1 = 0
fib2 = 1

n = abs(int(input()))

for i in range(n):
    if fib2 < n:
        print(fib2)
    fib1, fib2 = fib2, fib1 + fib2
