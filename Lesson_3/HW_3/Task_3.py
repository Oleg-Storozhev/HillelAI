# Дано матрицю N на M. Вивести транспоновану матрицю.
import numpy as np

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

for row in matrix:
    print(row)
rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("By lines:")
for row in rez:
    print(row)

matrix = np.column_stack(matrix)
print("By numpy\n", matrix.reshape(M,N))
