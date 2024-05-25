# mcdu = Milhar centena dezena unidade
def counting_sort(A, digito_MCDU):
    C = [0 for i in range(10)]
    B = [-1 for i in range(len(A))]

    for a in A:
        digito_significativos = (a // digito_MCDU) % 10
        C[digito_significativos] += 1
        

    for i in range(1, 10):
        C[i] = C[i] + C[i-1]

    for j in range(len(A)-1, -1, -1):
        digito_significativos = (A[j] // digito_MCDU) % 10
        posicao = C[digito_significativos] - 1
        B[posicao] = A[j]
        C[digito_significativos] -= 1
    
    return B

def radix_sort(l, n_digitos):
    for digito in range(n_digitos):
        l = counting_sort(l, 10**digito)
    return l

l = [481, 452, 351 , 282]
l = radix_sort(l, 3)

print(l)