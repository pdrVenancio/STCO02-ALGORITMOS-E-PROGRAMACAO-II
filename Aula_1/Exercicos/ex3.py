import random

#Essa função recebe 2 números grandes e devolve o ultimo digito do 
#   produtos desses dois números.
#Essa implementação está ineficiente e demora 40 segundos para executar
#   o programa. Uma implementação um pouco melhor pode fazer esse tempo 
#   cair pela metade. Melhore essa função e explique.

# def ult_dig_prod(a, b):
#     r = a * b
#     return r % 10

def ult_dig_prod(a, b):
    last_digit_a = a % 10
    last_digit_b = b % 10
    return (last_digit_a * last_digit_b) % 10

# Calculamos os últimos dígitos de a e b usando a operação % 10.
# Multiplicamos os dois últimos dígitos para obter o último dígito do produto.
# Retornamos esse último dígito.
# Essa abordagem é mais eficiente porque reduz a complexidade da operação de 
# multiplicação, focando apenas nos dígitos que realmente importam para determinar 
# o último dígito do produto. Isso elimina a necessidade de multiplicar números grandes, 
# o que pode ser muito demorado, especialmente para números com muitos dígitos.

#Não altere o programa daqui para baixo
random.seed(10)
soma = 0
for i in range(0, 1000000, 1):
    soma = soma + ult_dig_prod(random.randint(0, 10**2000), random.randint(0, 10**2000))  
print(soma)


