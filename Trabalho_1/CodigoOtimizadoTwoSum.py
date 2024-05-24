import random, time

#=====================================================================
def partition(l, first, last):
    # sorteamos um numero aleatorio da lista para evitar o caso da lista quase ordenada
    r = random.randint(first, last)
    l[first], l[r] = l[r] ,l[first]
    pivot = l[first]
    j = first + 1
    for  k in range(first + 1, last + 1):
        if l[k] < pivot:
            j = j + 1
            l[k], l[j - 1] = l[j - 1], l[k]

    l[first], l[j - 1] = l[j - 1], l[first]
    
    #posição em q esta o pivot
    return j - 1

def quick_sort(l, first , last):
    #print(l[first:last + 1])
    if first >= last:
        return 
    
    # p = posição do pivot
    p = partition(l, first, last)

    # ordenar 1 parte l[first: p - 1] 
    quick_sort(l, first, p - 1)

    # ordenar 2 parte l[p + 1 : last]
    quick_sort(l, p + 1, last)
    return l

#=====================================================================
tamanho = int(input("Digite o tamanho da lista: "))
# tamanho = 10
random.seed(tamanho)
l = []

# Gerando a lista de numeros alearorios
#=====================================================================
# Gerar uma lista ordenada de números de 0 a tamanho
# startTime = time.time()
for i in range(2**17):
    l.append(i)

# print(len(l))

# Embaralhar a lista
for i in range(tamanho):
    # Trocar o elemento atual com um elemento aleatório
    random_index = random.randint(0, 2**17 - 1)
    l[i], l[random_index] = l[random_index], l[i]

l = l[:tamanho]

print(l)

# endTime = time.time()
# print("Time part 01: " + str(endTime - startTime))
#=====================================================================

# o print abaixo mostra a lista depos de ser embaralhada
# print(l)

# Calculamos o numero alvo
#=====================================================================
alvo = random.randint(0, 2**17)
while alvo % 2 == 0:
    alvo = random.randint(0, 2**17)
#=====================================================================
# startTime = time.time()

# Ordenamos a lista pra calcular o numero de pares
l = quick_sort(l, 0, len(l) -1)

#print(len(l))
# print(l)

# Dois ponteiros para percorrer a lista
esquerda = 0
direita = len(l) - 1

# Contador de pares
contador = 0

# Verificamos a quantidade de pares percorrendo a lista do começo para o final
# e do final para o começo, até os ponteiros se encontrarem
while esquerda < direita:
    soma = l[esquerda] + l[direita]
    if soma == alvo:
        # print(l[direita], l[esquerda], alvo)
        contador += 1
        esquerda += 1
        direita -= 1
    elif soma < alvo:
        esquerda += 1
    else:
        direita -= 1

# Tempo parte 02
# endTime = time.time()
# print("Time part 02: " + str(endTime - startTime))

print(contador)