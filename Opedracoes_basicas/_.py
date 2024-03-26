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

######################################################################
# Dicionario

# Criar um dicionário
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Acessar um valor através da chave
value = my_dict['key1']

# Adicionar um novo par chave-valor
my_dict['new_key'] = 'new_value'

# Remover um par chave-valor
del my_dict['key1']

# Verificar se uma chave está presente
if 'key1' in my_dict:
    print("Key exists!")

# Iterar sobre chaves e valores
for key, value in my_dict.items():
    print(key, value)

# Obter todas as chaves ou valores
keys = my_dict.keys()
values = my_dict.values()

# Obter o número de pares chave-valor
num_items = len(my_dict)

# Copiar um dicionário
new_dict = my_dict.copy()

# Limpar todos os itens de um dicionário
my_dict.clear()

# Combinar dois dicionários
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Quando você usa ** com dicionários, ele 
#  desempacota os elementos do dicionário 
#  fornecido e os adiciona ao novo dicionário.
combined_dict = {**dict1, **dict2}

# Obter um valor padrão se a chave não existir
value = my_dict.get('key', 'default_value')

professor = {
    'nome' : 'hokama',
    'sala' : 30,
    'inst' : 'imc'
}

p2 = {
    'sala' : 31,
    'inst' : 'irn'
}

print(professor)

professor.update(p2)

print(professor)

#####################################################################
# Tuplas

# Criando uma tupla
tupla = (1, 2, 3, 4, 5)

# Acessando elementos
primeiro_elemento = tupla[0]
ultimo_elemento = tupla[-1]

# Fatiamento de tuplas
sub_tupla = tupla[1:3]

# Concatenação de tuplas
nova_tupla = tupla + (6, 7, 8)

# Verificando se um elemento está presente
if 5 in tupla:
    print("5 está na tupla")

# Tamanho da tupla
tamanho = len(tupla)

# Contagem de elementos
count = tupla.count(3)

# Encontrando o índice de um elemento
indice = tupla.index(4)

# Desempacotamento de tuplas
a, b, c, d, e = tupla

# Criando tuplas vazias
tupla_vazia = ()

# Convertendo outros tipos para tuplas
lista = [1, 2, 3]
tupla_da_lista = tuple(lista)

# Iterando sobre uma tupla
for item in tupla:
    print(item)

