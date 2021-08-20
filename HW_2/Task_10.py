# Дано число N і список з N чисел.
# Вивести список у зворотному порядку.

n = abs(int(input("Write how many numbers will you have on list: ")))
numbers = []
for i in range(n):
    numbers.append(float(input(str(i+1)+": ")))
numbers.reverse()
for i in range(n):
    print(numbers[i])
