class Arvore():
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []

def mostra(raiz, prefix):
    if raiz:
        print(prefix, end='')

    if raiz.direita:
        mostra(raiz.direita, prefix)

    if raiz.esquerda:
        mostra(raiz.esquerda, prefix)
        
def nivel(raiz, dado,nivel=0):
    if raiz is None:
        return 0
        
    if dado is None:
        return -1

    hesq = -1
    hdir = -1
    if raiz.esq:
        hesq = nivel(raiz.esq,dado,nivel+1) +1
    if raiz.dir:
        hdir = nivel(raiz.dir,dado,nivel+1)+1


    if hdir > hesq:
        return hdir
    else:
        return hesq
raiz = Arvore(5)
print(nivel(raiz,5))