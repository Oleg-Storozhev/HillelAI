# Дано число N і список з N чисел.
# Далі на вхід задаються пари чисел A,B>=0.
# Для кожної пари вивести значення списку з індексами від A включно до B не включно.
# Завершити роботу коли буде введено два нулі.
# Врахувати випадок коли A>B.

n = abs(int(input("How many number will you have?")))
numbers = []
for i in range(n):
    numbers.append(int(input(str(i+1)+": ")))

a = abs(int(input("A: ")))
b = abs(int(input("B: ")))

while a > 0 or b > 0:
    for i in range(a, b):
        print(numbers[i], end=", ")
    a = abs(int(input("A: ")))
    b = abs(int(input("B: ")))
