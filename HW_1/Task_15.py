def task_15(a ,b, c):
    a = abs(float(a))
    b = abs(float(b))
    c = abs(float(c))
    if a == 0 or b == 0 or c == 0:
        return "One of the sides is null"
    if a == b and a == c:
        return "right triangle"
    elif a == b or a == c or c == b:
        return "isosceles triangle"
    return "not right not isosceles"


assert task_15(3, 3, 3) == "right triangle"
assert task_15(3, 3, 1) == "isosceles triangle"
assert task_15(2, 3, 1) == "not right not isosceles"
assert task_15(2, 3, 0) == "One of the sides is null"
a, b, c = (input("Task 15. Enter 3 numbers: ").split())
print(task_15(a, b, c))
