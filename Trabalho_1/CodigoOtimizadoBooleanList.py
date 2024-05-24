# Pedro Venâncio dos Santos: 2023010066 // Breno Vieira Nogueira Carneiro: 2023003929

import random, time

# Esse codigo foi otimizado com a utilização de uma lista auxiliar, que verifica se seu índice (False por padrão)
# foi alterado para True, ou seja, se determinado número já foi sorteado, evitando duplicatas

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

tamanho = int(input())
# tamanho = 2 ** 17
random.seed(tamanho)
l = []

# Abaixo está presente a lista com False de 0 até tamanho + 1
# O "+ 1" é necessário pois o range vai de A até B, com B sendo exclusivo
presente = [False for i in range(0, 2**17 + 1)] # Usado para evitar duplicatas

# startTime = time.time()
while len(l) < tamanho:
    num = random.randint(0, 2**17)
    # Se presente[num] ja foi sorteado, esse número não é adicionado na lista
    if presente[num] == False: # Com o uso dessa lista, a verificação se torna O(1)
        # Se um número antes não sorteado for sorteado, mudamos o booleano no índice num para True na lista auxiliar
        presente[num] = True
        l.append(num)
# endTime = time.time()
# print("Time part 01: " + str(endTime - startTime))

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Nada foi alterado na escolha do número alvo (permaneceu igual ao código original)
# startTime = time.time()
# Sorteia um número entre 0 e 2**17 até que esse número seja ímpar
alvo = random.randint(0, 2**17)
while alvo % 2 == 0: 
    alvo = random.randint(0, 2**17)

# endTime = time.time()
# print("Time part 02: " + str(endTime - startTime))

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# startTime = time.time()
contador = 0

# Aqui é feita a contagem de quantos pares de números somados resultam em alvo
for num in l: # Iteramos cada número da lista de números sorteados anteriormente
    compl = alvo - num
    # Compl pode ser um número negativo. Em python, um número negativo significa a iteração
    # na lista ao inverso, ou seja, l[len(l) - 1] = l[-1]. Essa característica pode resultar em
    # um resultado True. Para evitar isso consideramos apenas compl maiores que zero.
    if compl >= 0 and presente[compl] == True:
        # Caso o complemento esteja na lista, e como i já está na lista (pois foi iterado), somamos 1 ao contador
        contador = contador + 1

# Como a soma é uma propriedade comutativa (A + B == B + A), um par é contado duas vezes. Para
# evitar esse problema, dividimos o resultado por dois
contador = contador / 2

# endTime = time.time()
# print("Time part 03: " + str(endTime - startTime))

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

print(int(contador))
