# Дано число N і список з N чисел.
# Для кожного числа зі списку вивести його відношення до середнього арифметичного цього списку (менше, дорівнює, більше).

n = abs(int(input()))
numbers = []
for i in range(n):
    numbers.append(float(input(str(i+1) + ": ")))

average = sum(numbers) / n

for i in range(n):
    if numbers[i] < average:
        print(numbers[i], "less then", average)
    elif numbers[i] > average:
        print(numbers[i], "more then", average)
    else:
        print(numbers[i], "the same as", average)
