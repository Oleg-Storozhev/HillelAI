# Написати функцію для знаходження відстані між двома точками в просторі: (x1, y1, z1) і (x2, y2, z2).
import math


def find(a, b):
    assert len(a) > 0 and len(b) > 0
    sum = (a[0]-b[0])**2 +(a[1]-b[1])**2 +(a[2]-b[2])**2
    return math.sqrt(sum)


a = [0,0,0]
b = [0,0,1]
assert find(a,b) == 1

a = [1,5,6]
b = [3,1,2]
print(find(a,b))
