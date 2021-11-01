class History:
    def __init__(self):
        self.history = []

    def push(self, item):
        self.history.append(item)

    def lastCommand(self):
        return self.history[-2]


class Player:
    def __init__(self):
        self.musics = []
        self.iteratorToPlay = 0
        self.isPlaying = False
        self.beforeElement = ''
        self.musicsPlaying = []

    # Começa a tocar as músicas da lista, na ordem da lista, a partir da música atual, caso já não esteja tocando (não tem efeito caso contrário).
    def play(self):
        self.musicsPlaying = self.musics[0:]
        self.isPlaying = True
        self.iteratorToPlay += 1

    # O codec responsável por reproduzir a música envia uma mensagem ended indicando que a reprodução dela terminou (obviamente, apenas uma música que estava sendo tocada pode terminar).
    def ended(self):
        self.iteratorToPlay += 1

    # Interrompe a execução da música atual.
    def stop(self):
        self.isPlaying = False

    # Acrescenta a música item ao final da lista.
    def addItem(self, item):
        self.musics.append(item)

    # Retira a primeira ocorrência da música item na lista, se houver e desde que não esteja tocando. Não interrompe a execução da música atual.
    def delItem(self, item):
        if item in self.musics:
            if item != self.musics[0]:
                self.musics.remove(item)

    # Define que a música item, se presente na lista, será a próxima a ser tocada, desde que não seja a que esteja sendo tocada no momento. A ocorrência de item na lista é realocada para tanto.
    def nextItem(self, item):
        if item in self.musics:
            if item != self.musics[self.iteratorToPlay]:
                self.beforeElement = self.musics.index(item)
                self.musics.remove(item)
                self.musics.insert(0, item)
            else:
                self.beforeElement = self.musics.index(item)
                self.musics.remove(item)
                self.musics.insert(1, item)

    # Mostra os items das músicas na lista, separados por vírgula, ou a mensagem "[vazia]" caso a lista esteja vazia.
    def list(self):
        if self.musics == []:
            print("[vazia]")
        else:
            print(*self.musics, sep=",")

    # Mostra o item da música atual (sendo tocada no momento), ou da próxima a ser tocada, caso nenhuma esteja no momento. Se a lista estiver vazia, apresente a mensagem: "Toque! Toque, Dijê!".
    def current(self):
        if self.musics == []:
            return "Toque! Toque, Dijê!"
        else:
            if self.iteratorToPlay <= 1:
                return self.musics[0]

            elif self.iteratorToPlay > 1:
                return self.musics[0]

            else:
                return self.musics[self.iteratorToPlay-1]

    # Desfaz o efeito de todas as instruções dadas até aquele ponto.
    def undoTotal(self):
        self.musics = []
        self.iteratorToPlay = 0
        self.isPlaying = False
        self.beforeElement = ''
        self.musicsPlaying = []

    # Desfaz os efeitos de uma instrução add, del, next ou play.
    def undo(self, lc):
        if lc[0] == "add":
            self.musics.pop()
        elif lc[0] == "del":
            self.musics.append(lc[1])
        elif lc[0] == "next":
            self.musics.pop(0)
            self.musics.insert(self.beforeElement, lc[1])
        elif lc[0] == "play":
            self.isPlaying = False
            self.iteratorToPlay -= 1

    def fight(self):
        return "Jedi Wagner, assuma o comando!"


player = Player()
commands = History()
while True:
    entry = input().split()
    commands.push(entry)
    if entry[0] == "play":
        player.play()
    elif entry[0] == "ended":
        player.ended()
    elif entry[0] == "stop":
        player.stop()
    elif entry[0] == "add":
        player.addItem(entry[1])
    elif entry[0] == "del":
        player.delItem(entry[1])
    elif entry[0] == "next":
        player.nextItem(entry[1])
    elif entry[0] == "list":
        player.list()
    elif entry[0] == "current":
        print(player.current())
    elif entry[0] == "undo":
        if "*" in entry:
            player.undoTotal()
        else:
            lastCommand = commands.lastCommand()
            player.undo(lastCommand)
    elif entry[0] == "fight":
        print(player.fight())
        break
