def recursaoCombinacao(valor, lista, usados, resultados, idx=0):
    if valor == 0:
        resultados.append(usados[:])
        return 1
    elif valor < 0 or idx >= len(lista):
        return 0
    
    usados[idx] += 1
    primeiroValor = recursaoCombinacao(valor - lista[idx], lista, usados, resultados, idx)

    usados[idx] -= 1
    segundoValor = recursaoCombinacao(valor, lista, usados, resultados, idx + 1)

    return primeiroValor + segundoValor

def main():
    lista_dinheiro = [100, 50, 20, 10, 5]
    resultados = []
    vezesAparecidas = [0, 0, 0, 0, 0]
    valor_conta = int(input())

    valor = recursaoCombinacao(valor_conta, lista_dinheiro, vezesAparecidas, resultados)

    print(f"Calculando possibilidades para o valor: {valor_conta}")
    if valor == 1:
        print("\nEssa foi fácil! Só existe 1 possibilidade de pagar essa conta.")
    elif valor == 0:
        print("\nInfelizmente, não há como pagar essa conta com as notas disponíveis.")

    print(f"\nTotal de possibilidades: {valor}")
    print("\nUso das notas:")
    
    for combinacao in resultados:
        for i in range(5):
            vezesAparecidas[i] += combinacao[i]

    print(f"R$100: usada em {vezesAparecidas[0]} combinações")
    print(f"R$50: usada em {vezesAparecidas[1]} combinações")
    print(f"R$20: usada em {vezesAparecidas[2]} combinações")
    print(f"R$10: usada em {vezesAparecidas[3]} combinações")
    print(f"R$5: usada em {vezesAparecidas[4]} combinações")

main()