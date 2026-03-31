# Exercício 1: Peça uma frase. O programa deve contar palavras e substituir "ruim" por "melhorável"
import re

def main():
    print()
    palavras = []
    palavras_limpas = []
    frase = input("Escreva a frase desejada contendo \"ruim\": ")
    palavras = frase.split()
    
    for n in palavras:
        ## testando o uso de .strip
        palavras_limpas.append(n.strip(",.;:!?"))
    print(f"Sua frase tem {len(palavras_limpas)} palavra(s)")
    print(frase.replace("ruim", "melhorável"))


if __name__ == "__main__":
    main()