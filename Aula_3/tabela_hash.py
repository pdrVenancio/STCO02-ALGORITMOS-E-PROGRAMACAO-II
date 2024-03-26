
print(ord('j'))
print(ord('o'))
print(ord('a'))
print(ord('o'))

end  = ord('j') + ord('o') + ord('a') + ord('o')

m = 100000
print( end % m)

#same -->

print(sum(map(ord, 'joao')))
print(sum(map(ord, 'aooj')))

def myHash(s):
    cont = 1
    valor = 0
    for c in s:
        valor = valor + (ord(c) * cont)
        cont += 1
    return valor

print(myHash('joao') % m)
print(myHash('aooj') % m)

print(myHash('ad') % m)
print(myHash('ga') % m)
