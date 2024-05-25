def merge(ord_l1, ord_l2):
    i = 0
    j = 0
    resultado = []
    while i < len(ord_l1) and j < len(ord_l2):
        if ord_l1[i] <= ord_l2[j]:
            resultado.append(ord_l1[i])
            i = i + 1
        else:
            resultado.append(ord_l2[j])
            j = j + 1
    while i < len(ord_l1):
        resultado.append(ord_l1[i])
        i = i + 1
    while j < len(ord_l2):
        resultado.append(ord_l2[j])
        j = j + 1
    
    return resultado

def merge_sort(l):
    if len(l) == 1:
        return l
    meio = int(len(l)/2)
    l1 = l[0:meio]
    l2 = l[meio:]
    print(l1)
    print(l2)

    l1 = merge_sort(l1)
    l2 = merge_sort(l2)

    print(l1)
    print(l2)

    return merge(l1, l2)

# Ordena a lista l do ini ao fim l[ini:fim] (exclusive fim)
def  insertion_sort(l, ini, fim):
    for i in range(ini + 1, fim):
        j = i
        valor = l[j]
        while j > ini and l[j-1] > valor:
            l[j] = l[j-1]
            j = j - 1
        l[j] = valor

#run tamanho das sublistas
def tim_sort(l, run):
    for x in range(0, len(l), run):
        insertion_sort(l, x, x + run)

    tamanho_bloco = run

    while tamanho_bloco < len(l):
        for x in range(0, len(l), tamanho_bloco * 2):
            l[x : x + 2 *tamanho_bloco] = merge(l[x : x + tamanho_bloco], l[x + tamanho_bloco : x + 2 * tamanho_bloco])
        
        tamanho_bloco = tamanho_bloco * 2
            
            

l =  [8, 5, 10, 9, 20, 30, 21, 13, 50, 70, 25, 14]

tim_sort(l, 4)
print(l)


