import math
def busca(lista, elemento):
        tamanho =  len(lista)
        for i in  range(0, tamanho, 1):
                if lista[i] == elemento:
                        return True
        return False


def busca_binaria(lista, elemento, ini, fim):
    if fim < ini:
           return False
    meio = math.floor((fim - ini ) / 2) + ini

    if lista[meio] == elemento:
        return True
    if lista[meio] > elemento:
           return busca_binaria(lista, elemento, ini, meio)
    
    if lista[meio] < elemento:
           return busca_binaria(lista, elemento, meio + 1, fim)
    return False
        

l = [5, 1, 20, 11, 8, 7, 9, 12]
l = sorted(l)
print(busca_binaria(l, 11, 0, len(l)))