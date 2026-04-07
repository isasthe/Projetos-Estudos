# Exercício 8:
#           Considerando dois vetores diferentes (mesma quantidade de elementos), calcule a distância euclidiana

from math import sqrt
import numpy as np 

def def_vetores():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    return a, b

def convert_list(lista):
    array = np.array(lista)
    return array

def euclid_dist(a, b):
    dist = sqrt(sum((a - b)**2))
    return dist

def main():
    a, b = def_vetores()
    a = convert_list(a)
    b = convert_list(b)
    distancia = euclid_dist(a, b)
    print(f"A distância euclidiana entre os vetores: \n     a = {a} \n     b = {b} \né {distancia}")

if __name__ == "__main__":
    main()