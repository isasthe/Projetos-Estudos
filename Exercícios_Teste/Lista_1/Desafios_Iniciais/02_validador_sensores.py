# Exercício 2: Leia 10 temperaturas. Se o valor for > 100 ou < -50, ignore-o. No final, mostre a média apenas dos valores válidos
def main():
    temperaturas = []
    print()
    for n in range(10):
        temp = (float(input(f"Digite a temperatura {n+1}: ")))
        if (temp <= 100 and temp >= -50):
            temperaturas.append(temp)
    print()
    if (len(temperaturas) > 0):
        media_temp = sum(temperaturas) / len(temperaturas)
        print(f"A média dos valores válidos é: {media_temp:.1f}")
    else:
        print("Você não digitou nenhuma temperatura válida")

if __name__ == "__main__":
    main()