import random


def task_8(a, b):
    return random.randint(int(a), int(b)), random.uniform(int(a), int(b))


test = task_8(5, 5)
assert test[0] == 5
assert test[1] == 5.0
a, b = (input("Task 8. Enter 2 numbers: ").split())
answer = task_8(a, b)
print(answer[0])
print(answer[1])
