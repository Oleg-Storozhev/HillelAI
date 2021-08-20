# Дано число N.
# Вивести перші N чисел Фібоначчі.

fib1 = 0
fib2 = 1

for i in range(abs(int(input()))):
    print(fib2)
    fib1, fib2 = fib2, fib1 + fib2
