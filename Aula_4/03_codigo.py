class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None for i in range(size)]
        self.count = 0

    def _hash(self, key):
        cont = 1
        valor = 0
        for c in key:
            valor = valor + (ord(c) * cont)
            cont = cont + 1
        return valor % self.size
        
    def put(self, key, value):
        item = HashItem(key, value)
        hashValue = self._hash(key)
        position = hashValue
        while self.slots[position] != None:
            if self.slots[position].key == key:
                break #Se a chave jÃ¡ existe vamos atualizar o value
            position = (position + 1) % self.size
        #colocar ou atualizar na posiÃ§Ã£o position.
        if self.slots[position] == None:
            self.count = self.count + 1
            self.check_growth()
        self.slots[position] = item
        
    def check_growth(self):
        loadfactor = self.count / self.size
        if loadfactor >= 0.75:
            self.growth()
        
    def get(self, key):
        hashValue = self._hash(key)
        position = hashValue
        while self.slots[position] != None:
            if self.slots[position].key == key:
                return self.slots[position].value
            position = (position + 1) % self.size
        return None
        
    def growth(self):
        new_size = 2 * self.size
        new_table = HashTable(new_size)
        for i in range(self.size):
            if self.slots[i] != None:
                #tenho que trazer da antiga 
                #tabela para a nova
                new_table.put(self.slots[i].key, self.slots[i].value)
        self.size = new_size
        self.slots = new_table.slots
        
    def __setitem__(self, key, value):
        self.put(key, value)
    def __getitem__(self, key):
        return self.get(key)
        
        

tabela = HashTable(10)

tabela.put("joao", 5)
tabela.put("ad", 6)
tabela.put("ga", 3)
tabela.put("joao", 4)

print(tabela.get("joao"))
print(tabela.get("ad"))
print(tabela.get("ga"))

tabela.put("adriano", 4)
tabela.put("amon", 7)
tabela.put("antony", 40)
tabela.put("augusto", 23)
tabela.put("beatriz", 42)
tabela.put("breno", 37)
tabela.put("bruno", 8)
tabela.put("carolina", 65)
tabela.put("daniel", 8)



for i in range(tabela.size):
    if tabela.slots[i] == None:
        print("Vazio")
    else:
        print(tabela.slots[i].key + " " + str(tabela.slots[i].value))




























