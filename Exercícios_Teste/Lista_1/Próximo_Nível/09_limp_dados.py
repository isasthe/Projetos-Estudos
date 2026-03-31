# Exercício 9:Receba uma lista de nomes digitados de qualquer jeito (ex: "  joão ", "MARIA", " ana  "). O programa deve devolver todos com a primeira letra maiúscula e sem espaços extras.

def recebe_num_nomes():
    while (True):
        try:
            contador = int(input("Quantos nomes terá a lista? "))
            if (contador > 0):
                break
            else:
                continue
        except ValueError:
            print("Valor Inválido. Tente novamente.")
            print()
    return contador

def normalizar_nome(nome):
    nome = nome.strip()
    nome = nome.title()
    return nome

def recebe_nome(contador):
    nomes = []
    for n in range(contador):
        nome = input(f"Qual o nome {n+1} da lista? ")    
        nome = normalizar_nome(nome)
        nomes.append(nome)
    return nomes

def formatar_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return ", ".join(lista[:-1])+" e "+ lista[-1]


def main():
    contador = recebe_num_nomes()
    print()
    nomes = recebe_nome(contador)
    print()
    if not nomes:
        print("Não há nomes válidos na lista")
    else:
        print(f"Os nomes da lista são: {formatar_lista(nomes)}")

if __name__ == "__main__":
    main()


        
