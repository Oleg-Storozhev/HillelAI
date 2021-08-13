def task_7(a, b):
    return float(a) + float(b), float(a) * float(b)


test = task_7(3, 7)
assert test[0] == 10.0
assert test[1] == 21.0
a, b = (input("Task 7. Enter 2 numbers: ").split())
answer = task_7(a, b)
print(answer[0])
print(answer[1])
