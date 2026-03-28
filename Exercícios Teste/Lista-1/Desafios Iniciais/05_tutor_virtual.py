# Exercício 5: Um loop que pergunta se o usuário entendeu. Se ele responder "não" 3 vezes, o programa encerra dizendo que chamará um humano.
import random

def main():
    frases = ["O laço for em Python é utilizado para percorrer sequências, como listas ou strings.", "Variáveis são espaços na memória do computador usados para armazenar dados.", "O if verifica uma condição: se ela for verdadeira, um caminho é seguido"]
    frase = random.choice(frases)
    contador = 0
    max_tentativas = 3
    while (True):
        print()
        print(frase)
        resposta = input("Você entendeu? (sim / não) ")
        if (resposta == "sim"):
            print("Que bom!! Encerrarei aqui então.")
            break
        elif (resposta == "não"):
            contador += 1
            if (contador == max_tentativas):
                print("Sinto muito você não ter conseguido entender. Vou te repassar para um humano.")
                print()
                break
            else:
                print("Que pena, vou repetir:")
        else:
            print("Resposta inválida. Irei repetir:")
        
if __name__ == "__main__":
    main()