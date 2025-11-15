#Mi = (Ci - Ki) mod 26
#Mi dividido por 26 deixa resto Ci - Ki

lista = []
def recursao(chaveInicial, fraseCriptografada, idx=0, mensagem=""):
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T' ,'U', 'V' ,'W', 'X', 'Y' ,'Z']
    if idx == len(fraseCriptografada):
        return mensagem
    if fraseCriptografada[idx] not in alfabeto:
        lista.append(idx)
    else:
        indiceLetra = alfabeto.index(chaveInicial)
        indiceCriptografia = alfabeto.index(fraseCriptografada[idx])
        resultado = (indiceCriptografia - indiceLetra) % 26
        chaveInicial = alfabeto[resultado]
        mensagem += chaveInicial

    return recursao(chaveInicial, fraseCriptografada, idx + 1, mensagem)

def main():
    chaveInicial = input().upper()
    fraseCriptografada = input().upper()

    print("Decifrando mensagem do Trickster...")
    mensagemDecifrada = recursao(chaveInicial, fraseCriptografada)
    
    if len(lista) == 0:
        print("Nenhuma armadilha encontrada! Até que o Trickster foi bonzinho.")
    else:
        print("Esse Trickster é um picareta mesmo. Foram encontradas armadilhas nas posições:", end="")
        for i in range(len(lista)):
            if i != len(lista) - 1:
                print(f" {lista[i]},",end="")
            else:
                print(f" {lista[i]}")
    print(f"Mensagem revelada: {mensagemDecifrada}")
main()

#D
#G
#6 - 3 mod 26 = 3
#