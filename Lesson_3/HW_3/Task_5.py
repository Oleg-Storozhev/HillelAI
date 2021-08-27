# Написати програму, що для заданого списку чисел визначає скільки в ньому унікальних значень.
import numpy as np

my_list = [0, 3, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 3, 4]
my_set = set(my_list)
print("Set", my_set, "=", len(my_set))

num = np.unique(my_list)
print("Numpy", num, "=", *num.shape)
