class ABB:
    def __init__(self, raiz, esquerda=None, direita=None):
        self.raiz = raiz
        self.esquerda = esquerda
        self.direita = direita

    def insertNode(self, dado):
        if dado.raiz <= self.raiz:
            if self.esquerda is None:
                self.esquerda = dado
            else:
                self.esquerda.insertNode(dado)
        else:
            if self.direita is None:
                self.direita = dado
            else:
                self.direita.insertNode(dado)

    def show(self, dado):
        print('(', end='')
        if dado:
            #print(f'{raiz.dado} ', end = '')
            print(dado.raiz, end='')
            print(' ', end='')
            if dado.esquerda:
                self.show(dado.esquerda)
                print(' ', end='')
            else:
                print('() ', end='')
            if dado.direita:
                self.show(dado.direita)
            else:
                print('()', end='')
            print(')', end='')

    def __str__(self, dado):
        return str(dado)


n = int(input())
if n != 0:
    dados = [ABB(int(x)) for x in input().split()]
    binTree = ABB(dados[0].raiz)
    dados = dados[1:]
    for i in range(len(dados)):
        binTree.insertNode(ABB(dados[i]))
    binTree.show(binTree)

else:
    print('()', end='')
