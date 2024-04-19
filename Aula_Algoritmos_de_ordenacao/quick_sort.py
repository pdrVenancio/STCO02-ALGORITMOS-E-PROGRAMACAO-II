import random

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
    print(l[first:last + 1])
    if first >= last:
        return 
    
    # p = posição do pivot
    p = partition(l, first, last)

    # ordenar 1 parte l[first: p - 1] 
    quick_sort(l, first, p - 1)

    # ordenar 2 parte l[p + 1 : last]
    quick_sort(l, p + 1, last)
    return

l = [30 ,91, 99, 7, 2, 71, 37 , 21, 13]
quick_sort(l, 0, len(l) -1)
print(l)
        