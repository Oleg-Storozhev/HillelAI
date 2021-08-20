# Написати програму, яка зчитує число,
# виводить його квадратний корінь і приймає наступне число.
# Програма повинна припинити роботу коли їй буде введено від’ємне число.
from math import sqrt

x = float(input("Write number: "))
while x >= 0:
    print("Square root of", x, "is", sqrt(x))
    x = float(input("Write number: "))


