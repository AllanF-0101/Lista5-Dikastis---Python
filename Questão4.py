def ehSeguro(linhaAtual, coluna, tabuleiro):
    contador = 0
    while contador < linhaAtual:
        if tabuleiro[contador] == coluna:
            return False
        distanciaLinhas = linhaAtual - contador
        distanciaColunas = coluna - tabuleiro[contador]
        if abs(distanciaLinhas) == abs(distanciaColunas):
            return False
        contador += 1
    return True

def backtracking(linhaAtual, alaOcupada, loteOcupado, n, tabuleiro):
    if linhaAtual == n:
        return 1
    
    totalSolucoes = 0

    for coluna in range(n):
        if not(linhaAtual == alaOcupada and coluna == loteOcupado):
            if ehSeguro(linhaAtual, coluna, tabuleiro):
                tabuleiro[linhaAtual] = coluna

                totalSolucoes += backtracking(linhaAtual + 1, alaOcupada, loteOcupado, n, tabuleiro)

                tabuleiro[linhaAtual] = -1
    return totalSolucoes

def main():
    n = int(input())
    ala_ocupada = 0
    lote_ocupado = 0
    var = True
    while var:
        ala_ocupada = int(input())
        lote_ocupado = int(input())
        if (ala_ocupada < 1 or ala_ocupada > n) or (lote_ocupado < 1 or lote_ocupado > n):
            print(f"Rogério e Chaguinha não encontraram o túmulo ocupado na posição ({ala_ocupada}, {lote_ocupado}). Assim eles nunca vão conseguir sair do cemitério!")
        else:
            print(f"Rogério e Chaguinha conseguiram encontrar o túmulo ocupado em ({ala_ocupada}, {lote_ocupado})!")
            print()
            var = False
    ala_ocupada -= 1
    lote_ocupado -= 1
    tabuleiro = [-1] * n

    total = backtracking(0, ala_ocupada, lote_ocupado, n, tabuleiro)
    print(f"Rogério e Chaguinha conseguiram encontrar {total} possíveis posições para as almas se posicionarem sem conflitos!")
    if total == 0:
        print("Não existe nenhuma configuração segura para as almas... Rogério e Chaguinha estão presos no meio da guerra das almas!")
    elif total <= 10:
        print("Os amigos vão precisar tomar muito cuidado para não pegar um caminho errado!")
    elif total <= 50:
        print("Uau! São tantas opções que eles até se perderam contando!")
    else:
        print("Em pleno Halloween e as almas descansando em paz! Rogério e Chaguinha vão conseguir sair logo do cemitério.")
main()