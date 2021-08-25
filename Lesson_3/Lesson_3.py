# Dictionary
print("DICTIONARY\n")

map = {"Soup": ["water", "potatoes"],
       "Pizza": ["salami", "cheese", "flover"],
       "Olive": ["potato", "cucumber", "oil", "tomato"]}

print(map.keys())
print(map.values())
print(map.items())

for key, v in map.items():
    print(key, end=": ")
    print(*v)

map["Soup"] = []
print(map)
map.pop("Soup")
print(*map)

# Set
print("\nSET\n")

s = set()
s2 = {5, 2, 3, "string"}
print(s2)

shop_1 = {"water", "crisps", "beer"}
shop_2 = {"cola", "sweet water", "nuts", "water"}

print(*shop_1 - shop_2)
print(*shop_2 - shop_1)
print(*shop_1 & shop_2)
print(*shop_1.intersection(shop_2))
print(*shop_2.symmetric_difference(shop_1))

# more methods: https://www.w3schools.com/python/python_ref_set.asp

# Numpy
print("\nNUMPY\n")
import numpy as np

a = np.array([[0,1,2],
              [1,2,3]])

b = np.array([[0,1],
              [1,2],
              [2,3]])

print(*a, "*", *b, "=", *np.dot(a, b))

print(a[-1, :])
print(b[-1, :])
print(sum(a[-1, :]))
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))

x = np.arange(6)
print(x.shape)
print(x)
x2 = x[np.newaxis, :]
print(x2)
print(x2.shape)
print(x2[:, -1])
x2 = x[:, np.newaxis]
print(x2)
print(x2.shape)
x2 = x2[:, np.newaxis]
print(x2.shape)

x = np.random.rand(3,2)  # 3,2 - shape
print(x)

# x = np.array([
#     [1,2,3],
#     [1,2,3,4],
#     [1,2]])
# print(x) <--- error (lists-or-tuples-or ndarrays with different lengths or shapes)


# https://numpy.org/doc/stable/user/quickstart.html
# https://numpy.org/doc/stable/user/absolute_beginners.html
