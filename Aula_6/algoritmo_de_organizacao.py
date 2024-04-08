import random
import time

def selection_sort(l):
    for i in range(len(l)):
        menor_indice = i
        for j in range(i+1, len(l)):
            if l[j] < l[menor_indice]:
                menor_indice = j
        
        #trocando as posições usando tuplas
        l[menor_indice], l[i] = l[i], l[menor_indice]
        
def bubble_sort(l):
    for i in range(len(l)):
        swap = 0
        for j in range(len(l) - 1, i, -1):
            if l[j-1] > l[j]:
                l[j-1],l[j] = l[j], l[j-1]
                swap =1
            if swap == 0:
                break

l = [random.randint(0, 99) for i in range(10)]
print(l)
selection_sort(l)
print(l)

l = [random.randint(0, 99) for i in range(10)]
print(l)
bubble_sort(l)
print(l)