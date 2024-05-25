import math

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i # J anda para trás
        valor = l[i]
        while j > 0 and l[j - 1] > valor:
            l[j] = l[j - 1]
            j = j - 1
        l[j] = valor
        
def bucket_sort(A):
    tamanho = len(A)
    buckets = [[] for i in range(tamanho)]

    for a in A:
        pos = math.floor(a * tamanho)
        buckets[pos].append(a)
    
    for i in range(0, tamanho):
        insertion_sort(buckets[i])
    
    lista_res = []
    for i in range(0 , tamanho):
        for b in buckets[i]:
            lista_res.append(b)

    return lista_res
        
    
l = [0.5, 0.4, 0.13, 0.12, 0.7]
l = bucket_sort(l)
print(l)

        