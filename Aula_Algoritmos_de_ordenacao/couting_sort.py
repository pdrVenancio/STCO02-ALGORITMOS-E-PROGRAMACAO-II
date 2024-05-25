
# A, B e C sao veroeres
def counting_sort(A, maior_valor):
    C = [0 for i in range(maior_valor +1)]
    B = [-1 for i in range(len(A))]

    for a in A:
        C[a] = C[a] + 1
        
    # Agora estamos fazendo algo interessante. Estamos atualizando os valores em C. 
    # Estamos somando o valor atual de C com o valor anterior de C.
    for i in range(1, maior_valor + 1):
        C[i] = C[i] + C[i-1]

    # Aqui é onde realmente organizamos nossos números. 
    # Estamos percorrendo nossa lista original de trás para frente.
    # Para preencher a lisata resultado de uma maneira Ordenação estavel 
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] =  C[A[j]] - 1
    
    return B

l = [2, 0, 3 ,4, 0 ,2]
l = counting_sort(l, 4)
print(l)