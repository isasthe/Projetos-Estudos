# Exercício 2:
    # Given this array: [[10, 20, 30],
 #                      [40, 50, 60],
 #                      [70, 80, 90]]
            # Get: Get: the element 50, the entire second row, the entire third column
            # Change 90 to 999

import numpy as np

array = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(array[1, 1])
print(array[1])
print(array[2])
array[2,2] = 999
print(array[2])
