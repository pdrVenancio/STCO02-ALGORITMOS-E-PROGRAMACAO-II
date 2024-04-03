# Aqui definimos um novo tipo de coisa chamado 'HashItem' que guarda um par de informações: uma chave e um valor.
class HashItem:
    # Isso é o que acontece quando criamos um novo HashItem.
    def __init__(self, key, value):
        # Cada HashItem tem uma chave (como uma palavra-chave) e um valor (como um número ou uma palavra).
        self.key = key
        self.value = value

# Aqui criamos uma nova coisa chamada 'HashTable'. É onde vamos guardar nossos HashItems.
class HashTable:
    # Quando criamos uma nova HashTable, precisamos dizer qual será o tamanho dela.
    def __init__(self, size):
        # Guardamos o tamanho que escolhemos.
        self.size = size
        # Criamos uma lista vazia com o mesmo tamanho da nossa tabela para guardar nossos HashItems.
        self.slots = [None for i in range(size)] # None é o mesmo que tabela vazia
        # Contamos quantos HashItems temos na tabela.
        self.count = 0
    
    # Aqui é onde escolhemos como vamos guardar nossos HashItems na tabela.
    def _hash(self, key):
        # Nós vamos transformar a chave em um número usando uma regra especial.
        cont = 1
        valor = 0
        for c in key:
            # Para cada letra na chave, pegamos o código dela e multiplicamos por um número.
            valor = valor + (ord(c) * cont)
            cont = cont + 1
        # Depois, dividimos esse número pelo tamanho da tabela e guardamos o resto.
        return valor % self.size
    
    # Aqui é onde colocamos um novo par de chave-valor na nossa tabela.
    def put(self, key, value):
        # Criamos um novo HashItem com a chave e o valor que queremos guardar.
        item = HashItem(key, value)
        # Descobrimos onde na tabela esse HashItem deve ficar.
        hashValue = self._hash(key)
        position = hashValue
        print(position)  # Printando a posição calculada
        # Se já tiver algo na posição, procuramos a próxima vaga.
        while self.slots[position] != None:
            if self.slots[position].key == key:
                break # Se a chave existe, vamos atualizar o value
            position = (position + 1) % self.size # Se chega no fim da tabela, volta ao inicio
            print(position)  # Printando nova posição em caso de colisão
        # Agora que achamos uma posição vazia, colocamos o novo HashItem lá.
        if self.slots[position] == None:
            self.count = self.count + 1
            self.check_growth()
        self.slots[position] = item

    # Aqui é onde verificamos se nossa tabela está ficando muito cheia, e se estiver, a fazemos crescer.
    def check_growth(self):
        loadfactor = self.count / self.size
        if loadfactor >= 0.75:
            self.growth()

    # Aqui é onde realmente fazemos a tabela crescer.
    def growth(self):
        # Duplicamos o tamanho da tabela.
        new_size = 2 * self.size
        # Criamos uma nova tabela com o novo tamanho.
        new_table = HashTable(2 * self.size)
        # Copiamos todos os HashItems da tabela antiga para a nova.
        for i in range(self.size):
            if self.slots[i] != None:
                new_table.put(self.slots[i].key, self.slots[i].value)
        # Agora que copiamos tudo, substituímos a tabela antiga pela nova.
        self.size = new_size
        self.slots = new_table.slots

# Agora que definimos como nossa tabela funciona, vamos criar uma e adicionar algumas coisas nela.
tabela = HashTable(10)

# Vamos adicionar alguns HashItems com suas chaves e valores.
tabela.put("joao", 5)
tabela.put("ad", 6)
tabela.put("ga", 3)
tabela.put("joao", 4)
tabela.put("joao1", 5)
tabela.put("joao2", 7)
tabela.put("joao3", 9)
tabela.put("joao4", 3)
tabela.put("joao5", 6)
tabela.put("joao6", 7)
tabela.put("joao7", 5)

# Agora, vamos pegar alguns valores usando suas chaves.
print(tabela.get("joao")) # Isso imprime o valor que tem a chave "joao".
print(tabela.get("ad"))   # Isso imprime o valor que tem a chave "ad".
print(tabela.get("ga"))   # Isso imprime o valor que tem a chave "ga".

# Finalmente, vamos fazer a tabela crescer e mostrar como ela está agora.
tabela.growth()

# Para cada posição na tabela, vamos ver se está vazia ou não e imprimir o que está lá.
for i in range(10):
    if tabela.slots[i] == None:
        print("Vazio")
    else:
        # Aqui só estamos mostrando o que está na tabela para ver como ela ficou.
        print(tabela.slots[i].key + " " + str(tabela.slots[i].value))

# Por algum motivo a variavel position não existe
