import math


def find(R):
    D = 2*R
    C = D * math.pi
    S = math.pi * R**2
    return D, C, S


result = find(abs(float(input("Enter radius of the circle: "))))

print("Diameter of the circle =", result[0], "units")
print("Circumference of the circle =", result[1], "units")
print("Area of the circle =", result[2], "sq. units")
