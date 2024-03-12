# veção python 3.11.3

#  LISTA

# Criar uma lista
minha_lista = [1, 2, 3, 4, 5]

# Acessar elementos da lista
print(minha_lista[0])  # Saída: 1
print(minha_lista[2])  # Saída: 3

# Alterar elementos da lista
minha_lista[1] = 10
print(minha_lista)  # Saída: [1, 10, 3, 4, 5]

# Adicionar elementos ao final da lista
minha_lista.append(6)
print(minha_lista)  # Saída: [1, 10, 3, 4, 5, 6]

# Remover elementos da lista
minha_lista.remove(3)  # Remove o elemento 3
print(minha_lista)  # Saída: [1, 10, 4, 5, 6]

# Verificar se um elemento está na lista
print(10 in minha_lista)  # Saída: True
print(7 in minha_lista)   # Saída: False

# Comprimento da lista
print(len(minha_lista))  # Saída: 5 (após a remoção do elemento 3)

# Iterar sobre uma lista
for elemento in minha_lista:
    print(elemento)

###################################################################
    
#  FILA
from queue import Queue

# Criar uma fila vazia
fila = Queue()

# Adicionar elementos à fila
fila.put(1)
fila.put(2)
fila.put(3)

# Verificar se a fila está vazia
print("A fila está vazia?", fila.empty())  # Saída: False

# Obter e remover o elemento mais antigo da fila (FIFO)
elemento = fila.get()
print("Elemento removido:", elemento)  # Saída: 1

# Verificar o tamanho da fila após a remoção
print("Tamanho da fila após a remoção:", fila.qsize())  # Saída: 2

# Obter e remover o próximo elemento da fila
elemento = fila.get()
print("Elemento removido:", elemento)  # Saída: 2

# Verificar o tamanho da fila após a segunda remoção
print("Tamanho da fila após a segunda remoção:", fila.qsize())  # Saída: 1

# Obter e remover o próximo elemento da fila
elemento = fila.get()
print("Elemento removido:", elemento)  # Saída: 3

# Verificar se a fila está vazia após a remoção de todos os elementos
print("A fila está vazia?", fila.empty())  # Saída: True

##############################################################################
# PILHA

# Criar uma pilha vazia
pilha = []

# Adicionar elementos à pilha
pilha.append(1)
pilha.append(2)
pilha.append(3)

# Exibir a pilha
print("Pilha completa:", pilha)  # Saída: [1, 2, 3]

# Remover o elemento do topo da pilha
elemento = pilha.pop()
print("Elemento removido:", elemento)  # Saída: 3

# Exibir a pilha após a remoção
print("Pilha após a remoção:", pilha)  # Saída: [1, 2]

# Adicionar mais um elemento à pilha
pilha.append(4)

# Exibir a pilha atualizada
print("Pilha atualizada:", pilha)  # Saída: [1, 2, 4]

#################################################################
# ARVORE DE BUSCA

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(valor, no_atual.esquerda)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(valor, no_atual.direita)
        else:
            # Valor já existe na árvore
            pass

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, no_atual):
        if no_atual is None:
            return False
        if valor == no_atual.valor:
            return True
        if valor < no_atual.valor:
            return self._buscar_recursivo(valor, no_atual.esquerda)
        else:
            return self._buscar_recursivo(valor, no_atual.direita)

# Exemplo de uso
arvore = ArvoreBinaria()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)

print(arvore.buscar(5))  # Saída: True
print(arvore.buscar(20)) # Saída: False
