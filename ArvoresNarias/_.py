import random
import time

l = []

start_time = time.time()
for _ in range(10_000):
    temp = [random.randint(0, 2**62) for _ in (10_000)]
    l.append(temp)

print("tempo gasto" + str(time.time() - start_time))

start_time = time.time()
contador = 0
for j in range(10_000):
    for i in range(10_000):
        if l[i][j] % 2 == 0:
            contador += 1

print("tempo gasto:" + str(time.time() - start_time))


start_time = time.time()
contador = 0
for i in range(10_000):
    for j in range(10_000):
        if l[i][j] % 2 == 0:
            contador += 1

print("tempo gasto:" + str(time.time() - start_time))