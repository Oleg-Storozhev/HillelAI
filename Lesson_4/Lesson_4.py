
# ЛИНЕЙНАЯ РЕГРЕССИЯ С 1 ПЕРЕМЕННОЙ

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
x = np.array([8, 6, 6, 6, 8, 8, 7, 7])
y = np.array([8, 8, 8, 8, 7, 8, 5, 4])

plt.scatter(x, y)


def guess(x, k, b):
    return k * x + b


model = LinearRegression()
model.fit(x.reshape(-1, 1), y)

y_guess = model.predict(x.reshape(-1, 1))
# y_guess = [guess(i, model.coef_[0], model.coef_) for i in x]
plt.plot(x, y_guess)
plt.show()
