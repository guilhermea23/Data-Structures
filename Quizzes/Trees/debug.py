class ArvoreBinaria:
    def __init__(self,raiz,esq=None,dir=None):
        self.raiz = raiz
        self.esq = esq
        self.dir = dir


def nivel(raiz,dado):
    esquerda,direita = -1,-1
    if raiz is None:
      return 0
    
    if dado is None:
        return -1
    
    if raiz:
        if raiz.dir:
            direita += nivel(raiz.dir, dado)
            return direita
        if raiz.esq:
            esquerda += nivel(raiz.esq, dado)
            return esquerda
    

raiz = ArvoreBinaria(1, ArvoreBinaria(2), ArvoreBinaria(3))

print(nivel(raiz,5))