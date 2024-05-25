import time, sys

# Ainda não é um algoritmo de ordenação
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

# A complexibilidade desse algoritmo é O(n logn)
# Quando a recursão é chamada a complexibilidade é logn
# Em cada nível das divisões da resursão, o merge acontece n vezes O(n / 2) que no fim é O(n)
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


# TESTE DA FUNÇÃO MERGE
l1 =[1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10, 12]
l = merge(l1, l2)
print(l)


# MERGE_SORT FUNCIONANDO
l = [7, 3 , 5, 1]
l = merge_sort(l)
print(l)

#CODIGO QUE VERIFICA TEMPO DE EXECUÇÃO DO CÓDIGO
# Codigo que lê um arquivo passado como segundo parâmetro
# Tem que ler rodar no terminal: python "nome_do_arquivo_python" "nome_da_lista_de_números"
f = open(sys.argv[1], "r") 
loriginal = f.read().split()

l = loriginal.copy()
# Lista exatamente reversa
# l.sort()
# l.reverse()

start_time = time.time()
l = merge_sort(l)
end_time = time.time()
print("O insertion_sort demorou" + str((end_time) - start_time))