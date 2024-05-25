import random

def main():
    random.seed(42)

    dimensao = 2000
    navios = 15000
    tiros = 15000

    listaA = set()
    listaB = set()

    acertoA = 0
    acertoB = 0
    tiroInutilA = 0 # quantos tiros acertaram navios já destruídos
    tiroInutilB = 0
    tiroAguaA = 0
    tiroAguaB = 0

    # jogador A coloca seus navios
    while len(listaA) < navios:
        x = random.randint(0, dimensao)
        y = random.randint(0, dimensao)
        if (x, y, 0) not in listaA:
            listaA.add((x, y, 0)) # 0 = não foi atingido

    # jogador B coloca seus navios
    while len(listaB) < navios:
        x = random.randint(0, dimensao)
        y = random.randint(0, dimensao)
        if (x, y, 0) not in listaB:
            listaB.add((x, y, 0)) # 0 = não foi atingido

    # jogador A atira
    for _ in range(tiros):
        x = random.randint(0, dimensao)
        y = random.randint(0, dimensao)
        if (x, y, 0) in listaB:
            # A acertou um navio de B
            acertoA += 1
            listaB.remove((x, y, 0))
            listaB.add((x, y, 1)) # 1 = foi atingido
        elif (x, y, 1) in listaB:
            # A atirou em um navio de B que já foi atingido
            tiroInutilA += 1
        else:
            # A atirou na água
            tiroAguaA += 1

    # jogador B atira
    for _ in range(tiros):
        x = random.randint(0, dimensao)
        y = random.randint(0, dimensao)
        if (x, y, 0) in listaA:
            # B acertou um navio de A
            acertoB += 1
            listaA.remove((x, y, 0))
            listaA.add((x, y, 1)) # 1 = foi atingido
        elif (x, y, 1) in listaA:
            # B atirou em um navio de A que já foi atingido
            tiroInutilB += 1
        else:
            # B atirou na água
            tiroAguaB += 1

    print("A acertou", acertoA, "navios de B")
    print("A atirou", tiroInutilA, "vezes em um navio de B que já foi atingido")
    print("A atirou", tiroAguaA, "vezes na água")
    print("B acertou", acertoB, "navios de A")
    print("B atirou", tiroInutilB, "vezes em um navio de A que já foi atingido")
    print("B atirou", tiroAguaB, "vezes na água")

if __name__ == '__main__':
    main()
