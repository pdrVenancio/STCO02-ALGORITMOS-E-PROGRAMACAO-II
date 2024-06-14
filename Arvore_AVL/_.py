class noh:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        self.altura = 0

# Para evitar falha de seguimentação na hora de calcular uma nova altura
def altura(no):
    if no == None:
        return -1
    else:
        return no.altura

def rotacionaDireita(raiz):
    nova_raiz = raiz.esq
    raiz.esq = nova_raiz.dir
    nova_raiz.dir = raiz
    
    raiz.altura = max(altura(raiz.esq), altura(raiz.dir)) + 1          
    nova_raiz.altura = max(altura(nova_raiz.esq), altura(nova_raiz.dir)) + 1          
    return nova_raiz

def rotacionaEsquerda(raiz):
    nova_raiz = raiz.esq
    raiz.esq = nova_raiz.dir
    nova_raiz.dir = raiz
    
    raiz.altura = max(altura(raiz.esq), altura(raiz.dir)) + 1          
    nova_raiz.altura = max(altura(nova_raiz.esq), altura(nova_raiz.dir)) + 1          
    return nova_raiz

def imprimeArvore(arvore):
    if arvore == None:
        return
    print('(', end='')
    imprimeArvore(arvore.esq)
    print(', ', str(arvore.dado), ", ", end='')
    imprimeArvore(arvore.dir)
    print(')', end='')
    return
    
    
arvore = noh(50)
arvore.esq = noh(47)
arvore.esq.esq = noh(45)


imprimeArvore(arvore)
print()
arvore = rotacionaDireita(arvore)
imprimeArvore(arvore)
print()