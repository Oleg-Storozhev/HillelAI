from math import sqrt


def task_5(a, b, c):
    a = abs(float(a))
    b = abs(float(b))
    c = abs(float(c))
    P = a + b + c
    p = P/2
    return P, sqrt(p*(p-a)*(p-b)*(p-c))


test = task_5(3, 3, 3)
assert test[0] == 9.0
assert test[1] == 3.897114317029974
a, b, c = (input("Task 5. Enter 3 numbers: ").split())
answer = task_5(a, b, c)
print("P =", answer[0], "\nS =", answer[1])
