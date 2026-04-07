# Exercício 10: Crie uma lista de 5 frases sobre IA. Peça para o usuário digitar uma palavra-chave. O programa deve exibir apenas as frases que contêm aquela palavra
from difflib import get_close_matches

def get_word():
    palavra = input("Digite uma palavra-chave para buscar dentre nosso banco de frases: ")
    return palavra

def base_frases_sinonimos():
    frases = ["A Inteligência Artificial utiliza algoritmos para processar dados."]
    frases.append("Modelos de aprendizado de máquina aprendem com padrões históricos.")
    frases.append("Redes neurais artificiais são inspiradas no cérebro humano.")
    frases.append("A IA pode ser usada para automação de tarefas repetitivas.")
    frases.append("A ética, hoje, é um pilar fundamental no desenvolvimento de novas IAs.")
    sinonimos = {"IA": ["inteligência artificial", "IA", "ias"], "machine learning": ["aprendizado de máquina", "machine learning"]}
    return frases, sinonimos

def check_sinonimos(palavra, sinonimos):
    palavra = palavra.lower()
    for n in sinonimos.keys():
        for m in sinonimos.get(n):
            m = m.lower()
            if palavra == m:
                termo = sinonimos.get(n)
                return termo
    return palavra

def format_palavras(termo, frases):
    frases_limpas = []
    busca = []
    for frase in frases:
        frases_limpas.append(frase.lower().replace(',', '').replace('.', ''))
    if isinstance(termo, list):
        for n in termo:
            n = n.lower().strip()
            busca.append(n)
    else:
        busca.append(termo.lower().strip())
    return frases_limpas, busca

def buscador(busca, frases_limpas):
    escolhidas = []
    contador = 0
    posicao_esc = []
    for frase in frases_limpas:
        for buscando in busca:
            if buscando in frase:
                escolhidas.append(frase)
                posicao_esc.append(contador)
        contador += 1
    return escolhidas, posicao_esc

def main():
    palavra_chave = get_word() #coletar a palavra chave não formatada
    frases, sinonimos = base_frases_sinonimos() # há a base de frases e de sinônimos
    termo = check_sinonimos(palavra_chave, sinonimos) # não tem ctz se é mais de uma palavra, ou é string ou é lista
    frases_limpas, busca = format_palavras(termo, frases) # todas as palavras em minúsculo e formatadas
    escolhidas, posicao_esc = buscador(busca, frases_limpas)
    if not escolhidas:
        print("Não foi possível encontrar nenhuma frase correspondente")
    else:
        print(f"As frases que tiveram conexão exata com sua palavra-chave (\"{palavra_chave}\") foram:")
        for n in posicao_esc:
            print(f"-> {frases[n]}")

if __name__ == "__main__":
    main()


        
    