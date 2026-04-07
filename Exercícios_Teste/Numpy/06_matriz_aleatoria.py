# Exercício 6:
#           Faça uma matriz 5x5 com números aleatórios e encontre o maior valor de cada coluna e de cada linha

import random
import numpy as np

def definir_matriz():
    matriz_list = []
    for n in range(5):
        linha = []
        for m in range(5):
            num = random.randint(0, 100)
            linha.append(num)
        matriz_list.append(linha)
    return matriz_list

def convert_list(lista):
    array = np.array(lista)
    return array

def busca_max_min(array):
    # axis = 0 -> buscar maior entre colunas
    max_colunas = array.max(axis = 0)
    # axis = 1 -> buscar maior entre linhas
    max_linhas = array.max(axis = 1)
    return max_colunas, max_linhas

def print_max(max_colunas, max_linhas):
    n = 0
    for v in max_colunas:
        n += 1
        print(f'O maior valor da coluna {n} é: {v}')
    print()
    n = 0
    for v in max_linhas:
        n+=1
        print(f'O maior valor da linha {n} é: {v}')


def main():
    matriz = convert_list(definir_matriz())
    print(f'A matriz 5x5 aleatória é: \n {matriz}')
    print()
    max_colunas, max_linhas = busca_max_min(matriz)
    print_max(max_colunas, max_linhas)

if __name__ == "__main__":
    main()
