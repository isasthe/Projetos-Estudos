# Exercise 3:
#       Convert to numpy array: a = [1, 2, 3, 4]
#                               b = [10, 20, 30, 40]
#       Compute:    a + b
#                   a * b
#                   a ** 2

import numpy as np

a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]

array_a = np.array(a)
array_b = np.array(b)

print(f'a = {array_a}')
print(f'b = {array_b}')
print()
print(array_a + array_b)
print()
print(array_a * array_b)
print()
print(array_a ** 2)
