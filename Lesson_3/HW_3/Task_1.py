# Дано число N і M. Далі вводяться N рядків по M чисел. Вивести M чисел, що відповідають значенням сум відповідних стовпчиків.
# Ввід:
# 2 3
# 1 2 3
# 4 5 6
# Вивід:
# 5 7 9
import numpy as np

def by_lists(mtx):
    answer = []
    for column in range(len(mtx[0])):
        total = 0
        for row in range(len(mtx)):
            total += mtx[row][column]
        answer.append(total)
    return answer


N = abs(int(input("How many rows will you have? ")))
M = abs(int(input("How many columns will be in one column? ")))

matrix = []
print("Enter the entries rowwise: ")

# For user input
for i in range(N):          # A for loop for row entries
    a = []
    print("row", i+1)
    for j in range(M):      # A for loop for column entries
         a.append(int(input("Column " + str(j+1) + ") ")))
    matrix.append(a)

print("Matrix:", matrix)
print("By lists: ", by_lists(matrix))
matrix = np.column_stack(matrix)
print("By numpy:", matrix.sum(axis=1))
