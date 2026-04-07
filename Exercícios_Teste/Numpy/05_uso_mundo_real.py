# Exercício 5:
#           Given the students grades: [7.5, 8.0, 6.5, 9.0, 5.5]
#               Caclule média, maior nota, menor nota, soma
#               Encontre todas as notas acima da média

import numpy as np

notas = np.array([[7.5, 8.0, 6.5, 9.0, 5.5]])

media = np.mean(notas)
maior = notas.max()
menor = notas.min()

print(f'A média das notas é: {media}')
print(f'A maior nota é: {maior}')
print(f'A menor nota é: {menor}')




