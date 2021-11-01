dictMorseToAlpha = {}
dictAlphaToMorse = {}


class Node():
    def __init__(self, dado='*', esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir


def encode(frase):
    pode = True
# codificar
    for letra in frase:
        if letra != ' ':
            if letra not in dictAlphaToMorse:
                pode = False
                break

    if pode:
        palavras = []

        frase = frase.split()
        for char in frase:
            if char == ' ':
                palavras.append('/')
            else:
                palavras.append([])

                for e in char:
                    palavras[-1].append(dictAlphaToMorse[e])

                palavras[-1] = ' '.join(palavras[-1])

        print(' /'.join(palavras))


def decode(mensagem):
    decoded = ''
    mensagem = mensagem.split()
    for letra in mensagem:
        if '/' in letra:
            letra = letra[1:]
            decoded += f' {dictMorseToAlpha[letra]}'
        elif letra in dictMorseToAlpha:
            decoded += dictMorseToAlpha[letra]
    return decoded


def isPossibleCode(mensagem):
    for l in mensagem:
        if l not in dictAlphaToMorse:
            if l != ' ':
                return False
    return True


def isPossibleDecode(mensagem):
    mensagem = mensagem.split()
    for l in mensagem:
        if l[0] == '/':
            l = l[1:]
        if l not in dictMorseToAlpha:
            return False
    return True


def insert(letra, morse, root):
    # . = esquerda
    # - = direita

    for tmp in morse:
        if tmp == '.':
            if root.esq:
                root = root.esq
            else:
                root.esq = Node()
                root = root.esq
        else:
            if root.dir:
                root = root.dir
            else:
                root.dir = Node()
                root = root.dir

    root.dado = letra


def bfs(node):
    queue = [node]

    while len(queue) != 0:
        node = queue[0]
        queue = queue[1:]

        if node:
            if node.dado != '*i':
                print(f' {node.dado}', end='')

            queue.append(node.esq)
            queue.append(node.dir)


n = int(input())
tree = Node('*i')
for i in range(n):
    letra, morse = input().split()
    dictMorseToAlpha[morse] = letra
    dictAlphaToMorse[letra] = morse
    insert(letra, morse, tree)

encodeConditional = int(input())
mensagem = ' '.join(input().split())

isPossibleCode = isPossibleCode(mensagem)
isPossibleDecode = isPossibleDecode(mensagem)

if encodeConditional == 1:
    if isPossibleCode == True:
        encode(mensagem)
    else:
        print('Impossível codificar a mensagem!', end='')

else:
    if isPossibleDecode == True:
        print(decode(mensagem), end='')
        print()
    else:
        print('Impossível decodificar a mensagem!', end='')

if isPossibleCode == True:
    print('*', end='')
    bfs(tree)
elif isPossibleDecode == True:
    print('*', end='')
    bfs(tree)
