def task_3(num):
    num = int(num)
    return num+1, num-1


test = task_3(5)
assert test[0] == 6
assert test[1] == 4
num = input("Task 3. Enter a number: ")
answer = task_3(num)
print("The next number for the number", num, " is", answer[0])
print("The previous number for the number", num, " is", answer[1])
