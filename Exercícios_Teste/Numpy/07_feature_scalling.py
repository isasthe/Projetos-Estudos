#Exercício 7: 
#               Tendo uma lista de no mínimo 5 dados (como alturas em cm), normalize os valores entre 0 e 1

import numpy as np

def quant_dados():
    quant = int(input("Quantos dados serão inseridos? "))
    return quant

def valor_dados(quant):
    valores = []
    for n in range(quant):
        valores.append(int(input(f"Digite a altura {n+1} em centímetros: ")))
    valores = np.array(valores)
    return valores

def normali_dados(valores):
    min = valores.min()
    max = valores.max()
    valores_norm = (valores - min) / (max - min)
    return valores_norm

def main():
    valores = valor_dados(quant_dados())
    print(valores)
    valores_norm = normali_dados(valores)
    print(valores_norm)

if __name__ == "__main__":
    main()