# Дано число N. Після чого в порядку обходу вводяться N пар координат многокутника на площині.
# Знайти периметр цього многокутника.
import math

n = abs(int(input("How many sides? ")))

if n < 3:
    print("No answer")

x, y = input("1: ").split()
x_0 = x = float(x)
y_0 = y = float(y)
answer = 0

for i in range(1, n):
    x_2 = x
    y_2 = y
    x, y = input(str(i+1) + ": ").split()
    x = float(x)
    y = float(y)
    answer = answer + math.sqrt((x_2 - x)**2 + (y_2 - y)**2)

answer = answer + math.sqrt((x_0 - x)**2 + (y_0 - y)**2)

print(answer)
