# Написати функцію, що отримує два відсортованих списки і об'єднує їх у новий відсортований список.

def unite(list_1, list_2):
    return sorted(list_1 + list_2)


a = [1,3,5]
b = [2,4,6]
assert unite(a,b) == [1,2,3,4,5,6]