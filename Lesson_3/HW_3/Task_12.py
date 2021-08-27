# Написати набір функцій для розрахунку наступних характеристик кола: діаметр, довжина й площа. Коло задається радіусом.
import math


def find(R):
    D = 2*R
    C = D * math.pi
    S = math.pi * R**2
    return D, C, S


r = 1
assert find(r) == (2.0, 6.283185307179586, 3.141592653589793)
print(find(abs(float(input()))))
