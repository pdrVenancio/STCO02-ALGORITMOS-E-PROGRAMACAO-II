import random

#Um sistema para verificação de fraudes consiste em contar em uma lista
#   de numeros, quantos terminam com 00, 01, 02 ... 99. Essa distribuição
#   normalmente vai ter uma forma constante e definida.
#A função abaixo devolve a lista com tal contagem, entretanto ela está 
#   bem ineficiente, levando quase 40 segundos para executar, uma 
#   implementação melhor vai gastar menos de 6 segundos. Melhore
#   essa função e explique.

# def conta_digitos_finais(lista):
#     lista_qtd_por_digito_final = []
#     for i in range(0, 100, 1):
#         qtd_terminando_em_i = 0
#         for v in lista:
#             if(v % 100 == i):
#                 qtd_terminando_em_i = qtd_terminando_em_i + 1
#         lista_qtd_por_digito_final.append(qtd_terminando_em_i)
#     return lista_qtd_por_digito_final


def conta_digitos_finais(lista):
#   Cria uma lista contendo 100 elementos, todos com o valor zero.
    lista_qtd_por_digito_final = [0] * 100
    for v in lista:
        ultimo_digito = v % 100
        lista_qtd_por_digito_final[ultimo_digito] += 1
    return lista_qtd_por_digito_final

# Nesta versão, ainda estamos iterando pela lista apenas uma vez. 
# Ao invés de usar um dicionário, estamos utilizando uma lista para armazenar 
# as contagens, onde cada posição corresponde a um dígito final (de 0 a 99).

# Essa abordagem direta e simples é eficiente porque evita o uso de estruturas 
# de dados mais complexas como dicionários e elimina a necessidade de conversão
# dos valores no final.

#Não altere o programa daqui para baixo
random.seed(10)
lista = random.sample(range(0, 100000000), 10000000)
print(conta_digitos_finais(lista))

