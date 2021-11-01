class No_ABB:
    def __init__(self, data):
        if data:
            self.data = data
            self.esquerda = None
            self.direita = None

    def __str__(self):
        return str(self.data)


class BinTree:
    def __init__(self, raiz=None):
        if raiz:
            self.raiz = No_ABB(raiz)
        else:
            self.raiz = None

    def mostra(self, raiz):
        print('(', end='')
        if raiz:
            #print(f'{raiz.dado} ', end = '')
            print(raiz.dado, end='')
            print(' ', end='')
            self.mostra(raiz.esq)
            print(' ', end='')
            self.mostra(raiz.dir)
            print(')', end='')


def altura(raiz):
    esquerda, direita = -1, -1
    if raiz is None:
        return 0
    else:
        if raiz.dir:
            direita = altura(raiz.dir)
        if raiz.esq:
            esquerda = altura(raiz.esq)
    if direita > esquerda:
        return direita+1
    else:
        return esquerda+1


# tree = BinTree()
# n1 = No_ABB('a')
# n2 = No_ABB('+')
# n3 = No_ABB('*')
# n4 = No_ABB('b')
# n5 = No_ABB('-')
# n6 = No_ABB('/')
# n7 = No_ABB('c')
# n8 = No_ABB('d')
# n9 = No_ABB('e')

# n6.esquerda = n7
# n6.direita = n8
# n5.esquerda = n6
# n5.direita = n9
# n3.esquerda = n4
# n3.direita = n5
# n2.esquerda = n1
# n2.direita = n3

# tree.raiz = n2


# tree.mostra()
# print()
