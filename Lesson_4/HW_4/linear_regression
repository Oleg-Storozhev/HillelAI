import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from scipy.optimize import minimize


def linear_regression(k, x, b):
    return k * x + b


def own_linear_regression(x, y):
    MSE = lambda a: sum(((a[1] * x + a[0] - y) ** 2) / len(x))
    MSE_min = minimize(MSE, [0, 0])
    y_predict = [linear_regression(MSE_min.x[1], i, MSE_min.x[0]) for i in x]
    model = MSE_min.x
    print("\nLinear regression (Own)")
    print("k =", model[1])
    print("b =", model[0])
    print(y_predict)
    print("C =", mean_squared_error(y, y_predict))
    plt.plot(x, y_predict, 'r')
    return MSE_min.x


def sklearn_linear_regression(x, y):
    model = LinearRegression()
    model.fit(x.reshape(-1, 1), y)
    y_predict = model.predict(x.reshape(-1, 1))
    print("\nLinear regression")
    print("k =", model.coef_[0])
    print("b =", model.intercept_)
    print(y_predict)
    print("C =",mean_squared_error(y, y_predict))
    plt.plot(x, y_predict, 'b')
    return model.intercept_, model.coef_[0]


def sklearn_ridge(x, y):
    model = Ridge()
    model.fit(x.reshape(-1, 1), y)
    y_predict = model.predict(x.reshape(-1, 1))
    print("\nRidge")
    print("k =", model.coef_[0])
    print("b =", model.intercept_)
    print(y_predict)
    print("C =",mean_squared_error(y, y_predict))
    plt.plot(x, y_predict, 'g')
    return model.intercept_, model.coef_[0]


def sklearn_lasso(x, y):
    model = Lasso()
    model.fit(x.reshape(-1, 1), y)
    y_predict = model.predict(x.reshape(-1, 1))
    print("\nLasso")
    print("k =", model.coef_[0])
    print("b =", model.intercept_)
    print(y_predict)
    print("C =",mean_squared_error(y, y_predict))
    plt.plot(x, y_predict, 'c')
    return model.intercept_, model.coef_[0]


x = np.array([8, 9, 8, 7])  # how many people come
y = np.array([5, 9, 7, 3])  # how many people made homework
x_input = abs(int(input("Write how many people in class now: ")))
plt.scatter(x, y)
answers = own_linear_regression(x, y)
print("Answer", abs(int(linear_regression(answers[1], x_input, answers[0]))))
answers = sklearn_linear_regression(x, y)  # Task 3 - Linear Regression by scikit-learn (BLUE COLOR)
print("Answer", abs(int(linear_regression(answers[1], x_input, answers[0]))))
answers = sklearn_ridge(x, y)  # GREEN COLOR
print("Answer", abs(int(linear_regression(answers[1], x_input, answers[0]))))
answers = sklearn_lasso(x, y)
print("Answer", abs(int(linear_regression(answers[1], x_input, answers[0]))))
plt.grid()
plt.show()
