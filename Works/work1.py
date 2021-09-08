class Player:
    def __init__(self):
        self.musics = []
        self.iteratorToPlay = 0

    # Começa a tocar as músicas da lista, na ordem da lista, a partir da música atual, caso já não esteja tocando (não tem efeito caso contrário).
    def play(self):
        print(self.musics([int(self.iteratorToPlay)]))
        int(self.iteratorToPlay) += 1

    # Interrompe a execução da música atual.
    def stop(self):
        pass

    # Acrescenta a música id ao final da lista.
    def addId(self, id):
        self.musics.append(id)

    # Retira a primeira ocorrência da música id na lista, se houver e desde que não esteja tocando. Não interrompe a execução da música atual.
    def delId(self, id):
        if id != self.musics[0]:
            self.musics.remove(id)

    # Define que a música id, se presente na lista, será a próxima a ser tocada, desde que não seja a que esteja sendo tocada no momento. A ocorrência de id na lista é realocada para tanto.
    def nextId(self, id):
        if id in self.musics:
            self.musics.pop(self.musics.index(id))
            self.musics.insert(0, id)

    # Mostra os ids das músicas na lista, separados por vírgula, ou a mensagem "[vazia]" caso a lista esteja vazia.
    def list(self):
        if self.musics == []:
            print("[vazia]")
        else:
            print(*self.musics, sep=",")

    # Mostra o id da música atual (sendo tocada no momento), ou da próxima a ser tocada, caso nenhuma esteja no momento. Se a lista estiver vazia, apresente a mensagem: "Toque! Toque, Dijê!".
    def current(self):
        if self.musics == []:
            return "Toque! Toque, Dijê!"
        else:
            pass

    def undo(self):
        pass

    def fight(self):
        return "Jedi Wagner, assuma o comando!"


player = Player()
while True:
    entry = input().split()
    if entry[0] == "add":
        player.play()

    elif entry[0] == "stop":
        player.stop()

    elif entry[0] == "add":
        player.addId(entry[1])

    elif entry[0] == "del":
        player.delId(entry[1])

    elif entry[0] == "next":
        player.nextId()

    elif entry[0] == "list":
        player.list()

    elif entry[0] == "current":
        print(player.current())

    elif entry == "undo *":
        player.undo()

    elif entry[0] == "fight":
        print(player.fight())
