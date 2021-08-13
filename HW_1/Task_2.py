def task_2(a, b, c):
    return float(a)+float(b)+float(c)


assert task_2(3, 3, 3) == 9.0
a, b, c = (input("Task 2. Enter 3 numbers: ").split())
print(task_2(a, b, c))
