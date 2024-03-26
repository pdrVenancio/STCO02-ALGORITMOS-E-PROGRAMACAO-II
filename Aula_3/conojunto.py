# conjunto

A = set ([1, 2, 3])

B = set([3, 4, 5])

#uniao
print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A & B)

print(A.symmetric_difference(B))
print(A ^ B)

print(A.issubset(B))
C = ([1, 2, 3, 4, 5])
print(A.issubset(C))

# Aceita varias coisas basta ser limitados e nao mutavel
A = set([1, 'string', (1, 2)])
print(A)


x = 45_000
A = set(range(0, x, 1))
for i in range(0, x + 10, 1):
    #A = A.union(set([i]))
    A.add(i)

print(len(A))

x1  = frozenset(['hokama'])
x2  = frozenset(['alg'])
x3  = frozenset([10])
xx = { x1, x2 , x3}
print(xx)