def task_10(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    return -1


assert task_10(-0.0000000000001) == -1
assert task_10(952424524) == 1
assert task_10(0) == 0
print(task_10(float(input("Task 10. Enter a number: "))))
