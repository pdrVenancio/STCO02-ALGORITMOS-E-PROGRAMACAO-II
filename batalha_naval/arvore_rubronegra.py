

class noh:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.atingido = False
        self.esq = None
        self.dir = None
        self.cor = True

def rotacionaEsquerda(a):
    b = a.dir
    a.dir = b.esq
    b.esq = a
    b.cor = a.cor
    a.cor = True
    return b

def rotacionaDireita(a):
    b = a.esq
    a.esq = b.dir
    b.dir = a
    b.cor = a.cor
    a.cor = True
    return b

def sobeVermelho(a):
    a.cor = True
    a.esq.cor = False
    a.dir.cor = False

def ehVermelho(a):
    if a == None:
        return False
    else:
        return a.cor

def ehNegro(a):
    if a == None:
        return True
    else:
        return a.cor == False


def insere_aux(raiz, dado):
    if raiz == None:
        return noh(dado)
    elif dado < raiz.dado:
        raiz.esq = insere_aux(raiz.esq, dado)
    elif dado > raiz.dado:
        raiz.dir = insere_aux(raiz.dir, dado)
    else:
        #jah existe esse dado, ignorar
        return raiz

    if ehVermelho(raiz.dir) and ehNegro(raiz.esq):
        raiz = rotacionaEsquerda(raiz)
    if ehVermelho(raiz.esq) and ehVermelho(raiz.esq.esq):
        raiz = rotacionaDireita(raiz)
    if ehVermelho(raiz.esq) and ehVermelho(raiz.dir):
        sobeVermelho(raiz)
    return raiz

def insere(raiz, dado):
    raiz = insere_aux(raiz, dado)
    raiz.cor = False
    return raiz

def busca(raiz, dado):
    if raiz == None:
        return raiz
    if dado < raiz.dado:
        return busca(raiz.esq, dado)
    if dado > raiz.dado:
        return busca(raiz.dir, dado)
    return raiz

# arvore = None

# arvore = insere(arvore, 5)
# arvore = insere(arvore, 7)
# arvore = insere(arvore, 3)

# no = busca(arvore, 5)
# if no != None:
# 	print(no.dado)
