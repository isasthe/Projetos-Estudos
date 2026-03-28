# Exercício 6: Modifique o exercício 2 para que, toda vez que uma temperatura for inválida, o programa escreva esse valor e o horário em um arquivo chamado erros.txt.
from pathlib import Path

def main():
    # encontrando onde está o arquivo .py que está rodando, para "erros.txt" ficar junto
    caminho_diretorio = Path(__file__).parent.absolute()
    # criando uma variável para facilitar encontrar "erros.txt"
    caminho_arquivo = caminho_diretorio / "erros.txt"
    
    temperaturas = []
    erros = []
    
    print()
    
    for n in range(10):
        temp = (float(input(f"Digite a temperatura {n+1}: ")))
        if (-50 <= temp <= 100):
            temperaturas.append(temp)
        else:
            erros.append(f"A temperatura {n+1} ({temp}°C) foi inválida\n")
    
    print()
    
    if (len(temperaturas) > 0):
        media_temp = sum(temperaturas) / len(temperaturas)
        print(f"A média das temperaturas válidas é: {media_temp:.1f}°C")
    else:
        print("Você não digitou nenhuma temperatura válida")
    
    print()
    
    print(f"A quantidade de erros foi: {len(erros)}")
    
    print()
    
    if (len(erros) > 0):
        # escrevendo no arquivo .txt || encoding para evitar erros com o uso de acentos (como em "inválida")
        with open(caminho_arquivo, 'w', encoding="utf-8") as t:
            t.writelines(erros)
        # lendo arquivo.txt || encoding para evitar erros com o uso de acentos (como em "inválida")
        with open(caminho_arquivo, 'r', encoding="utf-8") as t:
            for linha in t:
                print(linha)

if __name__ == "__main__":
    main()