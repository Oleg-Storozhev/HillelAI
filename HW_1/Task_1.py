def task_1(name):
    if len(name) == 0:
        return "please write the name!"
    return "Hello, " + name + "!"


assert task_1("Oleg") == "Hello, Oleg!"
assert task_1("") == "please write the name!"
print(task_1(input("Task 1. Your name is: ")))
