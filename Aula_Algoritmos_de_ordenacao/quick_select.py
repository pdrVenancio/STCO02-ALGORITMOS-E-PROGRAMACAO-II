# Procura o k-ésimo menor elemento

import random

def partition(l, first, last):
    
    r = random.randint(first, last)
    l[first], l[r] = l[r] ,l[first]
    pivot = l[first]
    j = first + 1
    for  k in range(first + 1, last + 1):
        if l[k] < pivot:
            j = j + 1
            l[k], l[j - 1] = l[j - 1], l[k]

    l[first], l[j - 1] = l[j - 1], l[first]
    
    return j - 1

def encontra_k(l,first, last, k):
    position_pivot = partition(l, first, last) 
    print(position_pivot, k)
    if k < position_pivot:
        #pega a lista da direita
        encontra_k(l, first, position_pivot - 1, k)
        #print("k <")
    elif k > position_pivot:
        #pega a lista da esquerda 
        encontra_k(l, position_pivot + 1, last, k )
        #print("k <")
    elif k == position_pivot:
        #achei o elemento
        print(f"elemento procurado {l[position_pivot]}")
        return


# k = Posição do menor elemento
k = 5
#l = random.sample(range(0,2**32), 300_000)
l = [30 ,91, 99, 7, 2, 71, 37 , 21, 13]
encontra_k(l,0, len(l)- 1, k)