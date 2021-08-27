# Написати програму, що для заданого списку слів підрахує кількість входжень кожного зі слів у цей список.

import numpy as np


def by_lists(list):
    for x in set(list):
        print(x, ":", list.count(x))


def by_numpy(list):
    unique, counts = np.unique(list, return_counts=True)
    return dict(zip(unique, counts))


my_list = [0, 3, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 3, 4]
print("By lists:")
by_lists(my_list)
a = np.array(my_list)
print("By numpy:", by_numpy(a))
