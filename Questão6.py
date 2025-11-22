def recursao(hora, energiaAtual, listaDeDecisoes, ativaGolden):
    melhorEnergiaHora = -1
    melhorDecisaoString = ""

    if hora == 6:
        resultadoFinal = listaDeDecisoes[:]
        resultadoFinal.insert(0, energiaAtual)
        return resultadoFinal
    
    for PE in [True, False]:
        for PD in [True, False]:
            for LZ in [True, False]:
                for CAM in [True, False]:
                    gastoAcao = 1
                    if PE:
                        gastoAcao += 7
                    if PD:
                        gastoAcao += 7
                    if LZ:
                        gastoAcao += 5
                    if CAM:
                        gastoAcao += 9

                    vivo = True
                    gastoCustos = 0
                    if (hora == 0 or hora == 3) and listaAux[0] > 0:
                        if PE or (LZ and not CAM):
                            gastoCustos += 3 + (listaAux[0] * 0.25)
                        else:
                            vivo = False
                    if (hora == 1 or hora == 4) and listaAux[1] > 0:
                        if PD or CAM:
                            gastoCustos += 2 + (listaAux[1] * 0.35)
                        else:
                            vivo = False
                    if vivo and hora == 4 and listaAux[3] > 0:        
                        if energiaAtual > 50:
                            if PE:
                                gastoCustos += 5 + (listaAux[3] * 0.15)
                            else:
                                vivo = False
                    if vivo and hora == 5 and listaAux[2] > 0:
                        if PE and PD or CAM:
                            gastoCustos += 3 + (listaAux[2] * 0.35)
                        else:
                            vivo = False
                    if vivo and hora == 5 and ativaGolden:
                        if CAM:
                            gastoCustos += 10 + (listaAux[2] * 1.95)
                        else:
                            vivo = False
    
                    if vivo:
                        energiaRestante = energiaAtual - (gastoAcao + gastoCustos)
                        if energiaRestante > melhorEnergiaHora:
                            melhorEnergiaHora = energiaRestante
                            porta_esq = "SIM" if PE else "NÃO"
                            porta_dir = "SIM" if PD else "NÃO"
                            luz = "SIM" if LZ else "NÃO"
                            cam = "SIM" if CAM else "NÃO"

                            melhorDecisaoString = f"0{hora}:00 AM -> PE: {porta_esq} | PD: {porta_dir} | LZ: {luz} | CAM: {cam}"

    if melhorEnergiaHora <= 0:
        return None
    nova_lista = listaDeDecisoes[:]
    nova_lista.append(melhorDecisaoString)
    
    return recursao(hora + 1, melhorEnergiaHora, nova_lista, ativaGolden)
niveisDificuldade = input().split()
foraDoIntervalo = False

energiaInicial = 100
todosSaoZero = False

sequenciaNumeros = ""
#Bonnie, Chica, Foxy, Freddy
listaAux = []

for valor in niveisDificuldade:
    sequenciaNumeros += valor
    if int(valor) < 0 or int(valor) > 20:
        foraDoIntervalo = True
    else:
        listaAux.append(int(valor))

GoldenFreddy = "1" in sequenciaNumeros and "9" in sequenciaNumeros and "8" in sequenciaNumeros and "7" in sequenciaNumeros

if sum(listaAux) == 0:
    todosSaoZero = True

if len(niveisDificuldade) == 4 and not foraDoIntervalo:
    #Colocar codigo aqui dentro
    if GoldenFreddy and "0" in sequenciaNumeros:
        print('''"IT'S ME"''')
    else:
        if todosSaoZero:
            print('"Uh, olá? Olá? Phone Guy falando. Não tem ninguém aqui..."')
        else:
            listaOrdenada = sorted(listaAux)
            goldenAtaca = (listaOrdenada == [1, 7, 8, 9])

            resultado = recursao(0, energiaInicial, [], goldenAtaca)

            if resultado is None:
                print('"Uh, Phone Guy falando. Uh, não tem mais ninguém do outro lado, não é?"')
            else:
                energiaFinal = resultado[0]
                caminho = resultado[1:]

                print(f'"Uh, olá? Ei, wow, dia sete, parabéns. E ainda com {energiaFinal:.2f}% de energia. Eu sabia que você conseguiria."')

                for linha in caminho:
                    print(linha)
else:
    print('"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."')