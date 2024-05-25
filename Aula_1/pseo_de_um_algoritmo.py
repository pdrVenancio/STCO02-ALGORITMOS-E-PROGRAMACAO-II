# c é um tempo que vai gastar para executar certa linha
l = [1,2,3,4,5, 2]
l2 = [6,7,8,9,0,1]

def soma(lista, tamanho):           #O(n)
    soma = 0                        #c1
    for i in range(0, tamanho, 1):  #c2 * n vezes
        soma += lista[i]            #c3 * n vezes
    return soma                     #c4

print(soma(l, len(l)))

def procura(lista, elemento):       #O(n)
    n = len(lista)                  #c1 O(1) 
    for i in range(0, n, 1):        #c2 * n vezes
        if lista[i] == elemento:    #c3 * n vezes
            return True             #c4 
    return False                    #c5

print(procura(l, 2))

def procura2(listaA, listaB, elemento): #O(tamanho da entrada da lista 1 + lista 2)
    for i in listaA:
        if i == elemento:
            return True
    
    for i in listaB:
        if i == elemento:
            return True

    return False

print(procura2(l, l2, 11))

def procura_comum(l1, l2):      #O(n^2)
    for i in l1:                #c1 * n vezes
        for j in l2:            #c2 * n ^ 2 vezes
            if i == j:          #c3 * n ^ 2 vezes
                return True
    return False
print(procura_comum(l, l2))

def procura_duplicados(lista):                   # O(n^2)
    n = len(lista)                               # O(1)
    for i in range(0, n, 1):                     # n vezes
        for j in range(0, n, 1):                 # n ^ 2 vezes
            #indice diferentes  porem o elemento igual
            if i != j and lista[i] == lista[j]:  # n ^ 2 vezes
                return True                      # O(1)
    return False                                 # O(1 )

print(procura_duplicados(l))

def procura_duplicados_otimizado(lista):         # O(n^2)
    n = len(lista)                               # O(1)
    for i in range(0, n - 1, 1):                 # n - 1 vezes
        for j in range(i + 1, n, 1):             # n - 1 + n - 2 ... + 1 = (n^2 - n)/2
            if i != j and lista[i] == lista[j]:  # Mesma coisa
                return True                      # O(1)
    return False                                 # O(1 )

print(procura_duplicados_otimizado(l))