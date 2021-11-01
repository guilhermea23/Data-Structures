class NodeTree:

    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __str__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)


def inserirABB(raiz, nodo):

    if raiz is None:
        raiz = nodo

    elif nodo.chave > raiz.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            inserirABB(raiz.direita, nodo)
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            inserirABB(raiz.esquerda, nodo)


entrada = ''
comandos = []
lista = []
while entrada != 'quack':
    result1 = ''
    result2 = ''
    result3 = ''
    entrada = str(input())
    if entrada != 'in' and entrada != 'pre' and entrada != 'pos' and entrada != 'quack':
        lista.append(int(entrada))
    else:
        comandos.append(entrada)

    for x in (sorted(lista)):
        result1 += str(x) + ' '
    if entrada == 'in':
        print(result1)

    if entrada == 'pre' and lista != []:
        copia2 = lista.copy()
        raiz = NodeTree(lista[0])
        copia2.pop(0)
        for i in copia2:
            inserirABB(raiz, NodeTree(i))

        aux1 = []

        def pos_ordem(raiz):
            if not raiz:
                return
            aux1.append(raiz.chave)
            pos_ordem(raiz.esquerda)
            pos_ordem(raiz.direita)

        pos_ordem(raiz)
        for j in aux1:
            result2 += str(j) + ' '
        print(result2)
    if entrada == 'pos' and lista != []:
        copia = lista.copy()
        raiz = NodeTree(lista[0])
        copia.pop(0)
        for i in copia:
            inserirABB(raiz, NodeTree(i))

        aux = []

        def pos_ordem(raiz):
            if not raiz:
                return
            pos_ordem(raiz.esquerda)
            pos_ordem(raiz.direita)
            aux.append(raiz.chave)

        pos_ordem(raiz)

        for k in aux:
            result3 += str(k) + ' '
        print(result3)
    if entrada == 'pre' and lista == []:
        print('')
    elif entrada == 'pos' and lista == []:
        print('')
