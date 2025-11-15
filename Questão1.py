def recursao(numero, valorMaximo):
    if numero == 0:
        return 1
    if numero < 0 or valorMaximo < 1:
        return 0

    return recursao(numero - valorMaximo, valorMaximo) + recursao(numero, valorMaximo - 1)
doces = int(input())
resultado = recursao(doces, doces)

print("DOCES OU TRAVESSURAS???")
print(f"sem travessuras por hoje! tenho {resultado} sacolinhas pra vocês")
if resultado % 2 == 0:
    print("doces equilibrados, sem travessuras!")
else:
    print("hmm... número ímpar de sacolinhas 🍭 cuidado com as bruxas!")