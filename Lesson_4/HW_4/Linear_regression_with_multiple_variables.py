import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from scipy.optimize import minimize


def linear_regression(x1, x2, x3, x4, k1, k2, k3, k4, b):
    return k1 * x1 + k2 * x2 + k3 * x3 + k4 * x4 + b


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
    return MSE_min.x


def sklearn_linear_regression(x, y):
    model = LinearRegression()
    model.fit(np.transpose(x), y)
    y_predict = model.predict(np.transpose(x))
    print("\nLinear regression")
    print("k1 =", model.coef_[0])
    print("k2 =", model.coef_[1])
    print("k3 =", model.coef_[2])
    print("k4 =", model.coef_[3])
    print("b =", model.intercept_)
    print("Predict =", *y_predict)
    print("C =",mean_squared_error(y, y_predict))
    return model.coef_, model.intercept_


def sklearn_ridge(x, y):
    model = Ridge()
    model.fit(np.transpose(x), y)
    y_predict = model.predict(np.transpose(x))
    print("\nRidge")
    print("k1 =", model.coef_[0])
    print("k2 =", model.coef_[1])
    print("k3 =", model.coef_[2])
    print("k4 =", model.coef_[3])
    print("b =", model.intercept_)
    print("Predict =", *y_predict)
    print("C =", mean_squared_error(y, y_predict))


def sklearn_lasso(x, y):
    model = Lasso()
    model.fit(np.transpose(x), y)
    y_predict = model.predict(np.transpose(x))
    print("\nLasso")
    print("k1 =", model.coef_[0])
    print("k2 =", model.coef_[1])
    print("k3 =", model.coef_[2])
    print("k4 =", model.coef_[3])
    print("b =", model.intercept_)
    print("Predict =", *y_predict)
    print("C =", mean_squared_error(y, y_predict))


people = [8, 9, 8, 7]
hard = [0, 2, 3, 4]  # from 0 to 10
math_level = [0, 1, 1, 3]  # from 0 to 5
python_level = [0, 1, 2, 4]  # from 0 to 5


x = np.array([people, hard, math_level, python_level])
y = np.array([5, 9, 7, 3])  # how many people made homework
sklearn_linear_regression(x, y)  # blue
sklearn_ridge(x, y)  # green
sklearn_lasso(x, y)  # cyan
