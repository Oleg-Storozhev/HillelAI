# Дано число N і список з N чисел.
# Вивести всі числа, що більші від обох своїх сусідніх у списку.

n = abs(int(input()))
numbers = []
for i in range(n):
    numbers.append(float(input(str(i+1) + ": ")))

for i in range(1, n-1):
    if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
        print(numbers[i], end=" ")
