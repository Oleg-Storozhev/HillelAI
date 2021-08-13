def task_11(num_1, num_2, act):
    if act == "+":
        return float(num_1) + float(num_2)
    elif act == "-":
        return float(num_1) - float(num_2)
    elif act == "*":
        return float(num_1) * float(num_2)
    elif act == "/":
        return float(num_1) / float(num_2)
    return "I don't know what do you want"


assert task_11(3, 3, "*") == 9.0
assert task_11(3, 3, "Hello! It's me!") == "I don't know what do you want"
n_1, n_2, a = (input("Task 11. Enter 2 numbers and 1 action: ").split())
print(task_11(n_1, n_2, a))
