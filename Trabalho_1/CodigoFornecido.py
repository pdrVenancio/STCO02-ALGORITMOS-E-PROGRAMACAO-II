import random, time

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

tamanho = 2**17
random.seed(tamanho)
l = []

startTime = time.time()
while len(l) < tamanho:
    num = random.randint(0, 2**17)
    if num not in l:
        l.append(num)
endTime = time.time()
print("Time part 01: " + str(endTime - startTime))
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

startTime = time.time()
alvo = random.randint(0, 2**17)
while alvo % 2 == 0:
    alvo = random.randint(0, 2**17)

print(alvo)

endTime = time.time()
print("Time part 02: " + str(endTime - startTime))

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

startTime = time.time()
contador = 0
for i in l:
    compl = alvo - i
    if compl in l:
        contador = contador + 1

endTime = time.time()
print("Time part 03: " + str(endTime - startTime))

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

print(int(contador/2))

print(contador)