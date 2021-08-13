from math import sqrt


def task_4(num):
    return sqrt(abs(float(num)))


assert task_4(9) == 3.0
assert task_4(-9) == 3.0  # Protection from minus values
print("Side of the square", task_4(input("Task 4. Enter a square area: ")))
