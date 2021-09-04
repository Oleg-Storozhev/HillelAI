
# ЛИНЕЙНАЯ РЕГРЕССИЯ С N ПЕРЕМЕННОЙ

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# x = np.array([8, 6, 6, 6, 8, 8, 7, 7], [0, 0, 0, 1, 1, 1, 2, 2])
# y = np.array([8, 8, 8, 8, 7, 8, 5, 4])
x = np.array([[8, 9, 8, 7], [0, 2, 3, 4]])
y = np.array([5, 9, 7, 3])

# plt.scatter(np.transpose(x), y)


# def guess(x1, x2, m, k, b): # х1 - кол-во людей, х2 - сложность, у - сделало людей (m,k,b) - нез коофиценты
#     return k * x1 + m * x2 + b


model = LinearRegression()
model.fit(np.transpose(x), y)

print("k =", model.coef_[0])
print("m =", model.coef_[1])
print("b =", model.intercept_)
y_guess = model.predict(np.transpose(x))
print("C =",mean_squared_error(y, y_guess))
# y_guess = [guess(i, 1, model.coef_[0], model.coef_[1], model.intercept_) for i in x[0]]
print(y_guess)

plt.plot(np.transpose(x), y_guess)
plt.show()
