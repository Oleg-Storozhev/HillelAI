def task_6(sum, procent):
    sum = abs(float(sum))
    procent = abs(float(procent))
    sumWithProc = sum * procent/100
    return sum + sumWithProc, sumWithProc


test = task_6(100, 10)
assert test[0] == 110.0
assert test[1] == 10.0
test = task_6(-100, -10)
assert test[0] == 110.0
assert test[1] == 10.0
a, b = (input("Task 6. Enter 2 numbers: ").split())
answer = task_6(a, b)
print(answer[0])
print(answer[1])
