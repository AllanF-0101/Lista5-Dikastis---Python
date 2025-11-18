#23:59
#2
#0S
#0B
'''
00S0
A000
00A0
B000
'''

def backtracking(matriz, x_byte, y_byte, tempoMinutos, movimentosFeitos, tamanhoMapa):
    if x_byte < 0 or x_byte >= tamanhoMapa or y_byte < 0 or y_byte >= tamanhoMapa:
        return -1
    if movimentosFeitos > tempoMinutos:
        return -1
    if matriz[x_byte][y_byte] == "A":
        return -1
    if matriz[x_byte][y_byte] == "V":
        return -1
    if matriz[x_byte][y_byte] == "S":
        return movimentosFeitos
    
    matriz[x_byte][y_byte] = "V"

    resultado_cima = backtracking(matriz, x_byte - 1, y_byte, tempoMinutos, movimentosFeitos + 1, tamanhoMapa)
    resultado_baixo = backtracking(matriz, x_byte + 1, y_byte, tempoMinutos, movimentosFeitos + 1, tamanhoMapa)
    resultado_direita = backtracking(matriz, x_byte, y_byte + 1, tempoMinutos, movimentosFeitos + 1, tamanhoMapa)  
    resultado_esquerda = backtracking(matriz, x_byte, y_byte - 1, tempoMinutos, movimentosFeitos + 1, tamanhoMapa)

    resultados = []
    if resultado_cima != -1:
        resultados.append(resultado_cima)
    if resultado_baixo != -1:
        resultados.append(resultado_baixo)
    if resultado_direita != -1:
        resultados.append(resultado_direita)
    if resultado_esquerda != -1:
        resultados.append(resultado_esquerda)
    matriz[x_byte][y_byte] = "0"
    if resultados:
        return min(resultados)
    else:
        return -1
    
horario = input().split(":")
tempo = int(horario[1]) if int(horario[1]) >= 10 else int(horario[1][1])
minutosRestantes = 60 - tempo
print(f"O relógio marca 23 horas e {tempo} minuto(s)! Byte tem apenas {minutosRestantes} minuto(s) para escapar!")

matriz = []
posicaoByte = []
posicaoSaida = []

tamanhoMapa = int(input())

for i in range(tamanhoMapa):
    linha = input()
    for j in range(len(linha)):
        if linha[j] == "B":
            posicaoByte = [i, j]
        if linha[j] == "S":
            posicaoSaida = [i, j]
    matriz.append(list(linha))

resultado = backtracking(matriz, posicaoByte[0], posicaoByte[1], minutosRestantes, 0, tamanhoMapa)
analise = minutosRestantes - resultado

if resultado == -1 or analise < 0:
    print("NÃÃÃÃO! Tudo isso por causa de um docinho! Você estará para sempre conosco, Byte!")
else:
    print(f"CONSEGUIMOS!! Byte precisou de {resultado} minuto(s) para conseguir escapar!")
    if analise > 10:
        print(f"Abóboras CInistras que nada! Byte mostrou quem é que manda e conseguiu sair faltando {minutosRestantes - resultado} minutos para elas acordarem")
    else:
        print(f"Ufa! Essa foi por pouco! Mas com ajuda dos alunos de IP essas abóboras nem pareciam tão sinistras assim.")

