# Exercício 4: Peça uma frase e imprima cada palavra separada por letras. Ex: "IA" vira I-A.

def main():
    frase = input("Digite a frase a ser tokenizada: ")
    palavras = frase.split()
    
    print()

    for palavra in palavras:
        palavra_limpa = palavra.strip(",.;:!?")
        print("-".join(palavra_limpa))

if __name__ == "__main__":
    main()
    