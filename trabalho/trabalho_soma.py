# dar 3 soluçoes diferentes para melhorar esse codigo
# 1 tem que envolver tabela hash
# pode ser em dupla

import random
#tamanho = int(input())
random.seed(2**17)
tamanho = 2**17

l = []

while len(l) < tamanho:
    num = random.randint(0, 2**17)
    if num not in l:
        l.append(num)

alvo = random.randint(0, 2**17)
while alvo % 2 == 0:
    alvo = random.randint(0, 2**17)
    

contador = 0

for i in l:
    complemento = alvo - i
    if  complemento in l:   
        contador = contador + 1
        #print(i, complemento)
    
print(int(contador/2))