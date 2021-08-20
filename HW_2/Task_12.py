# Дано число N і список з N чисел.
# Вивести всі числа, що зустрічаються у списку лише раз.

def Only_once(lst):
    answ = []
    for i in lst:
        if lst.count(i) == 1:
            answ.append(i)
    return answ


n = abs(int(input("Write how many numbers will you have on list: ")))
numbers = []
for i in range(n):
    numbers.append(float(input(str(i+1)+": ")))

print(*Only_once(numbers))
