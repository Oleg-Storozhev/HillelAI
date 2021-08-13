from math import sqrt


def task_12(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c
    if(D > 0):
        x_1 = (-b + sqrt(D)) / 2*a
        x_2 = (-b - sqrt(D)) / 2*a
        return "Two answers:\nx_1 = " + str(x_1) + "\nx_2 = " + str(x_2)
    if(D == 0):
        x = -b/2*a
        return "One answer:\nx = " + str(x)
    return "No answers"


assert task_12(1, 2, 1) == "One answer:\nx = -1.0"
assert task_12(1, 3, 2) == "Two answers:\nx_1 = -1.0\nx_2 = -2.0"
a, b, c = (input("Task 12. Enter 3 numbers: ").split())
print(task_12(a, b, c))
