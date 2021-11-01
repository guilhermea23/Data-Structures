class Editor:
    def __init__(self):
        self.items = []

    def addInit(self, item):
        self.items.insert(0, item)

    def addEnd(self, item):
        self.items.append(item)

    def removeEnd(self):
        return self.items.pop()

    def removeInit(self):
        return self.items.pop(0)

# Não tá achando o item
    def removeThis(self, item):
        return self.items.remove(item)

# Não tá mudando o item
    def alterThis(self, old_item, new_item):
        self.items.remove(self.items.index(old_item))
        self.items.insert(self.items.index(old_item), new_item)

    def show(self):
        print(*self.items, sep='\n')


s = Editor()
while True:
    command = input().split()
    if command[0] == 'X':
        break

    elif command[0] == 'I':
        s.addInit(command[1])

    elif command[0] == 'F':
        s.addEnd(command[1])

    elif command[0] == 'P':
        print(s.removeEnd())

    elif command[0] == 'D':
        print(s.removeInit())

    elif command[0] == 'E':
        print(s.removeThis(command[1]))

    elif command[0] == 'T':
        s.alterThis(command[1], command[2])
