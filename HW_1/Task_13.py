def task_13(min, SMS):
    min = abs(float(min))
    SMS = abs(int(SMS))
    answer = 30.0
    if min > 100:
        answer += (min - 100) * 0.3
    if SMS > 30:
        answer += (SMS - 30) * 0.25
    return answer


assert task_13(100, 30) == 30.0
assert task_13(-100, -30) == 30.0
assert task_13(101, 30) == 30.3
assert task_13(100, 31) == 30.25
a, b = (input("Task 13. Enter 2 numbers: ").split())
print(task_13(a, b))
