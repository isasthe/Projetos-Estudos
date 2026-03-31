# Exercício 3: Crie uma lista com suas habilidades e outra com os requisitos da vaga. Exiba o que você já tem e o que falta.
def formatar_lista(lista):
    if not lista:
        return ">nenhuma<"
    if len(lista) == 1:
        return lista[0]
    return ", ".join(lista[:-1])+" e "+ lista[-1]

def main():
    hab_user = []
    hab_vaga = []
    hab_tem = []
    hab_falta = []
    
    print()
    
    while (True):    
        hab = input(f"Digite uma habilidade sua: (-1 para sair) ")
        if (hab == "-1"):
            break
        else:
            hab_user.append(hab)
    
    print()
    
    while (True):
        hab = input(f"Digite uma habilidade exigida na vaga: (-1 para sair) ")
        if (hab == "-1"):
            break
        else:
            hab_vaga.append(hab)
    
    print()
    
    for hab in hab_vaga:
        if hab in hab_user:
            hab_tem.append(hab)
        else:
            hab_falta.append(hab)
    
    print(f"As habilidades necessárias que você já tem são: {formatar_lista(hab_tem)}")
    print(f"As habilidades exigidas pela vaga que você não tem são: {formatar_lista(hab_falta)}")

if __name__ == "__main__":
    main()