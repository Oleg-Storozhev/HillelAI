# Дано число N, список з N чисел, число M і далі список з M чисел.
# Вивести всі числа, які трапляються в обох списках.


n = abs(int(input("Write how many numbers will you have on list N: ")))
N = []
for i in range(n):
    N.append(float(input(str(i+1)+": ")))

n = abs(int(input("Write how many numbers will you have on list M: ")))
M = []
for i in range(n):
    M.append(float(input(str(i+1)+": ")))

answ = list(set(N) & set(M))
print(answ)
