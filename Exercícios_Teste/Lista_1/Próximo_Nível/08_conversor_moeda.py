# Exercício 8: Crie um programa que converta o valor da sua bolsa (R$ 1.500,00) para Dólar
import requests

def pedir_salario():
    while (True):
        try:
            salario = float(input("Qual o seu salário? "))
            break
        except ValueError:
            print("Valor Inválido. Tente Novamente:")
            print()
    return salario

def consultar_conversao():
    real_dolar = requests.get("https://economia.awesomeapi.com.br/json/BRL-USD")
    if real_dolar.status_code == 200:
        real_dolar = real_dolar.json()
        cotacao = float(real_dolar[0]["bid"])
        return cotacao
    else:
        print()
        print("Erro. Infelizmente não foi possível consultar a conversão, tente novamente mais tarde.")
        return None

def conversao(salario, cotacao):
    sal_convertido = salario * cotacao
    return sal_convertido

def main():
    salario = pedir_salario()
    cotacao = consultar_conversao()
    if cotacao is not None:
        sal_convertido = conversao(salario, cotacao)
        print()
        print(f"A cotação de BRL-USD é de: {cotacao}")
        print(f"Seu salário de R${salario:.2f} em dolár é ${sal_convertido:.2f}")

if __name__ == "__main__":
    main()


