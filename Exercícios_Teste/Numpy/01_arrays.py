# Exercício 1:
    # Create and print their shapes:
                # a 1D array with numbers from 1 to 5
                # a 2D array (3x3) filled with zeros
                # a 2D array (2x4) filled with ones  

import numpy as np

array1 = np.array([[1,2,3,4,5]])
array2 = np.zeros((3, 3))
array3 = np.ones((2, 4))

print(array1)
print(np.shape(array1))
print()
print(array2)
print(np.shape(array2))
print()
print(array3)
print(np.shape(array3))