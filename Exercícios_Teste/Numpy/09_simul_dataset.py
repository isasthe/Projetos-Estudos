# Exercício 9
#              com uma array de dados, a primeira coluna diz respeito a idade e a segunda aos salários
#   1. extraia apenas idades, apenas salários, 
#   2. calcular a idade média, o salário médio
#   3. normalize (entre 0 e 1) apenas a coluna de salários

import numpy as np

def nova_linha():
    print()

def definir_dados():
    array = np.array([[25, 5000], [30, 6000], [22, 4500], [40, 8000],])
    return array

def extrair_dados(array):
    idades = array[::, 0]
    salarios = array[::, 1]
    return idades, salarios

def media_dados(dados):
    media = dados.mean()
    return media

def normalizar_dado(dados):
    min_d = dados.min()
    max_d = dados.max()   
    normalizado = (dados - min_d) / (max_d - min_d)
    return normalizado

def shape_dado_indiv(dados):
    len_dados = dados.size
    shape_dados = dados.reshape(len_dados, 1)
    return shape_dados

def main():
    array = definir_dados()
    print(f'Os dados são:\n{array}')
    idades, salarios = extrair_dados(array)
    nova_linha()
    print(f'As idades são: {idades}')
    print(f'Os salários são: {salarios}')
    idade_media = media_dados(idades)
    salario_media = float(media_dados(salarios))
    nova_linha()
    print(f'A média de idade é {idade_media} anos e a média de salário é R${salario_media:.2f}')
    salarios_norm = shape_dado_indiv(normalizar_dado(salarios))
    nova_linha()
    print(f'Os salários normalizados são:\n{salarios_norm}')

if __name__ == "__main__":
    main()