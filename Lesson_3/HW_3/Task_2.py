# Дано число N. Створити й вивести двовимірний масив розмірністю N на N, у якого на основній діагоналі розташовані одиниці,
# а всі інші значення дорівнюють нулю.
# Ввід:
# 3
# Вивід:
# 1 0 0
# 0 1 0
# 0 0 1

import numpy as np

def by_lists(n):
    answer = []
    for i in range(n):
        a = []
        for j in range(n):
            if j == i:
                a.append(1)
            else:
                a.append(0)
        answer.append(a)
    return answer


N = abs(int(input()))
print("By lists:", by_lists(N))
a = np.zeros((N, N), int)
np.fill_diagonal(a, 1)
print("By numpy:\n", a)
