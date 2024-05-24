# Pedro Venâncio dos Santos: 2023010066 // Breno Vieira Nogueira Carneiro: 2023003929

# random (utilizada para aleatorizar os números da lista e o alvo)
# time (para contar o tempo de cada sessão do código em testes)
import random, time

# DUAS CLASSES FORAM USADAS NESSE CÓDIGO. ABAIXO, ESTÃO CADA UMA DESSAS CLASSES IMPLEMENTADAS E COMENTADAS PASSO A PASSO
# ==========================================================================================================================
class HashTable:
    # Os atributos padrões que um objeto HashTable recebe ao ser criado
    def __init__(self, size):
        self.size = size # O tamanho da hashTable
        self.slots = [None for i in range(size)] # Uma lista com tamanho size vazia
        self.count = 0 # Conta quantos elementos a hashTable possui a medida que novos elementos são adicionados
    
    # Aqui deve ser escolhido um método de resolução de conflitos
    def _hash(self, key):
        cont = 1
        valor = 0
        # O for abaixo aleatoriza um índice numérico em que um item vai ser armazenado na hash
        # com base no ASCII desse item (usando a função ord())
        for c in str(key):
            valor = valor + (ord(c) * cont)
            cont = cont + 1
        return valor % self.size # Devolve o valor dentro dos limites da tabela
    
    def put(self, key, value):
        item = BinaryTree(key, value) # Cria uma árvore binária básica com valores passados
        hashValue = self._hash(key) # encontra o hash da key passada acima
        position = hashValue # Armazena a nova key na variavel position para melhor legibilidade de código
        if self.slots[position] is None: # Caso o índice da hash está vazio uma árvore é atribuída aquele índice
            self.slots[position] = item
            self.count += 1  # Incrementa quando uma nova árvore é criada
        else:
            # Verifica se a chave já está na árvore binária, um novo valor é adicionado e count precisa ser incrementado
            if self.slots[position].getTree(key) is None:
                self.count += 1  # Incrementa quando um novo nó é adicionado
            # Caso o if acima n seja executado, o valor daquela chave é apenas atualizado (no caso quando o número sorteado
            # é repetido), e o count n precisa ser incrementado
            self.slots[position].putTree(key, value)

    # Acha uma key que contém uma ávore binária, busca na árvore e retorna o valor procurado
    def get(self, key):
        position = self._hash(key)
        if self.slots[position] != None:
            return self.slots[position].getTree(key) #Esse get é uma funcao presente na árvore binaria NAO É RECURSÃO
        return None
    
    def __setitem__(self, key, value): # A sintaxe (hashTable[x] = y) passa a chamar a função put
        self.put(key, value)
    
    def __getitem__(self, key): # A sintaxe (hashTable[x] = y) passa a chamar a função get
        return self.get(key)

class BinaryTree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    
    def putTree(self, key, value):
        if self.key == key: # Se a key for igual, apenas atualiza o valor (numeros repetidos nesse caso)
            self.value = value
        if self.key > key: # Se a chave passada for menor, um novo nó é criado à esquerda do nó atual (caso n exista)
            if self.left == None:
                self.left = BinaryTree(key, value)
            else:
                self.left.putTree(key, value) # Caso exista um nó à esquerda, essa mesma função é chamada recursivamente
        if self.key < key: # Se a chave passada for maior, um novo nó é criado à direita do nó atual (caso n exista)
            if self.right == None:
                self.right = BinaryTree(key, value)
            else:
                self.right.putTree(key, value) # Caso exista um nó à direita, essa mesma função é chamada recursivamente
        return
    
    # procura um valor e o retorna
    def getTree(self, key):
        if self.key == key: # Caso a chave procurada seja encontrada, seu valor é retornado
            return self.value
        elif self.key > key: # Caso a chave procurada seja menor que a atual, o nó da esquerda é chamado
            if self.left is None: # Se estiver vazio retorna None
                return None
            return self.left.getTree(key) # Senão chama a função recursivamente para o nó da esquerda
        else: # Caso a chave procurada seja maior que a atual, o nó da direita é chamado
            if self.right is None: # Se estiver vazio retorna None
                return None
            return self.right.getTree(key) # Senão chama a função recursivamente para o nó da direita
# ==========================================================================================================================

# Esse código foi otimizado com a utilização da Tabela Hash, que utiliza em cada índice presente na tabela uma árvore binária.
# Por conta da utilização da árvore binária, o tamanho da tabela nunca se altera e não precisamos aumentá-la em tempo de execução

tamanho = int(input())
# tamanho = 10000
random.seed(tamanho)

# Primeiro criamos uma tabela hash com um tamanho de 100 (Pode ser alterado, mas preferimos manter esse número)
hash_table = HashTable(100)

startTime = time.time()
while hash_table.count < tamanho:
    # Quando um número é adicionado na tabela, se ele já existe, seu valor é "atualizado", ou seja
    # o atributo count não se altera. Isso evita duplicatas
    num = random.randint(0, 2**17)
    hash_table[num] = num
endTime = time.time()
# print("Time part 01: " + str(endTime - startTime))

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Nada foi alterado na escolha do número alvo
startTime = time.time()
alvo = random.randint(0, 2**17)
while alvo % 2 == 0: # Um número entre 0 e 2**17 é sorteado até que esse número seja ímpar
    alvo = random.randint(0, 2**17)

endTime = time.time()
# print("Time part 02: " + str(endTime - startTime))

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

startTime = time.time()
contador = 0
# Para todos os números entre 0 e alvo (pois somente pares de números menores que alvo podem satisfazer esse problema)
for i in range(0, alvo):
    if hash_table[i] != None: # Se i estiver na tabela
        compl = alvo - i
        # Compl pode ser um número negativo e a comparação se ele é positivo ou não nesse momento polpa um pouco de tempo,
        # evitando que a função get seja chamada
        if compl >= 0 and hash_table[compl] != None:
            # Caso o complemento esteja na lista, e como i já está na lista, somamos o contador
            contador = contador + 1

# Como a soma é uma propriedade comutativa (A + B == B + A), um par é contado duas vezes. Para
# evitar esse problema, dividimos o resultado por dois
contador = contador / 2

endTime = time.time()
# print("Time part 03: " + str(endTime - startTime))

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

print(int(contador))
