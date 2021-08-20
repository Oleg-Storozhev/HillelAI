# Реалізуйте CRM систему, яка повинна приймати й обробляти запити наступних видів:
# Додати працівника з іменем <name> у систему.
# add
# <name>
# Перевірити чи є працівник з іменем <name> у системі.
# find
# <name>
# Вивести список всіх працівників.
# list
# Видалити працівника з іменем <name> із системи.
# delete
# <name>
# Завершити роботу системи.
# stop
s = ""
list = []
while s != "stop":
    s = str(input("Write the command: "))
    if s == "add":
        list.append(str(input("Write the name: ")))
    elif s == "find":
        print(str(input("Write the name: ")) in list)
    elif s == "list":
        print(*list)
    elif s == "delete":
        list.remove(str(input("Write the name: ")))
