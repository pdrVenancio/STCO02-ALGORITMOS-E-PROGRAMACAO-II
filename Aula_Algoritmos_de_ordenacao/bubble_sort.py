import random
import time

def bubble_sort(l):
    for i in range(len(l)):
        #flag se ouve troca de posição
        swap = 0
        for j in range(len(l) - 1, i, -1):
            if l[j-1] > l[j]:
                l[j-1],l[j] = l[j], l[j-1]
                swap =1
            if swap == 0:
                break

l = [random.randint(0, 99) for i in range(10)]
print(l)
bubble_sort(l)
print(l)