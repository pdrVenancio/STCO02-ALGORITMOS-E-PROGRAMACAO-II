import random, time
import sys

# Complexibilidade é O(n^2)
def insertion_sort(l):
    for i in range(1, len(l)):
        # Talvez o l[i] esteja no lugar errado
        j = i # J anda para trás
        valor = l[i]
        while j > 0 and l[j - 1] > valor:
            l[j] = l[j - 1]
            j = j - 1
        l[j] = valor

# l = [15, 5, 20, 45, 50]
# insertion_sort(l)
# print(l)

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
insertion_sort(l)
end_time = time.time()
print("O insertion_sort demorou" + str((end_time) - start_time))
