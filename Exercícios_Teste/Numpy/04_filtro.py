# Exercício 4:
#       Tendo: arr = [5, 10, 12, 7, 8, 20, 18, 3, 15, 6]
#          crie duas arrays, uma apenas com números maiores que 10 e outra apenas com números pares

import numpy as np

arr = [5, 10, 12, 7, 8, 20, 18, 3, 15, 6]
arr_10 = []
arr_par = []

for n in arr:
    if n > 10:
        arr_10.append(n)

arr_10 = np.array(arr_10)
print(arr_10)

for n in arr:
    if (n % 2 == 0):
        arr_par.append(n)
arr_par = np.array(arr_par)
print(arr_par)