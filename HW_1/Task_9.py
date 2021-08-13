def task_9(a, b):
    if float(a) < float(b):
        return a
    return b


assert task_9(3, 4) == 3
a, b = (input("Task 9. Enter 2 numbers: ").split())
print(task_9(a, b))
