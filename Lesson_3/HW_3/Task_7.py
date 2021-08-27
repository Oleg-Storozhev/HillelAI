# Написати програму, що дозволить підтримувати список електронних адрес для розсилки.
# Програма повинна дозволяти додавати, перевіряти наявність і видаляти електронні адреси.

s = ""
set = set()
while s != "stop":
    s = str(input("Write the command: "))
    if s == "add":
        set.add(str(input("Write the email: ")))
    elif s == "find":
        print(str(input("Write the email: ")) in set)
    elif s == "delete":
        set.remove(str(input("Write the email: ")))
