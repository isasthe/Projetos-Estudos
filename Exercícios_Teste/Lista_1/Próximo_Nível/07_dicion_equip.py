# Exercício 7: Em vez de listas separadas para nome e valor, use um Dicionário para armazenar o inventário do laboratório. O programa deve permitir buscar o preço pelo nome do item
def cadastrar_equipamentos():
    n = 0
    equipamentos = {}
    num_equip = int(input("Quantos equipamentos serão registrados? "))
    while n < num_equip:
        nome_equip = input(f"Qual o nome do equipamento {n+1}? ")
        if nome_equip not in equipamentos: # verificar a exclusão
            valor_equip = float(input(f"Qual o valor do(a) {nome_equip}? "))
            equipamentos[nome_equip] = valor_equip
            n += 1
        else:
            print("Esse equipamento já existe. Tente novamente.")
    return equipamentos

def buscar_equipamentos(equipamentos):
    while(True):
        print(f"Sabendo que os equipamentos são: {list(equipamentos)}")
        busca = input(f"Digite o nome de um equipamento para saber seu valor: ")
        if (busca in equipamentos):
            print(f"O valor do(a) {busca} é R${equipamentos[busca]:.2f}")
            break
        else:
            print("Nome inválido. Tente novamente.\n")

def main():
    equipamentos = cadastrar_equipamentos()
    print()
    buscar_equipamentos(equipamentos)

if __name__ == "__main__":
    main()