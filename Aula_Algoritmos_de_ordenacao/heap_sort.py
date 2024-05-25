def desce_heap(l, pai, tamLista): # o primero pai é a raiz
    # Se o l[i] é menor que o maior dos filhos
    esquerdo = 2 * pai + 1
    direito = 2 * pai + 2

    if esquerdo >= tamLista:
        return
    maior_filho = esquerdo

    if direito < tamLista and l[direito] > l[esquerdo]:
        maior_filho = direito

    if l[pai] < l[maior_filho]:
        l[pai], l[maior_filho] = l[maior_filho], l[pai]
        desce_heap(l, maior_filho, tamLista)

# A complexibilidade desse algoritmo é O(nlogn)
def heap_sort(l):
    tamLista = len(l)
    # Como todas as folhas da árvore são heaps perfeitos:
    # Pelo menos metade dos nós da árvore são folhas, então o range pode começar por len(l) / 2
    for i in range(int(tamLista/2), -1, -1): #O segundo parâmetro é exclusivo e recebe -1 poderemos acessar l[0]
        desce_heap(l, i, tamLista)

    for i in range(len(l) - 1, 0, -1):
        l[0], l[i] = l[i], l[0]
        tamLista = tamLista - 1
        desce_heap(l, 0, tamLista)



lista = [81, 99, 10, 11, 7, 71]

heap_sort(lista)
print(lista)