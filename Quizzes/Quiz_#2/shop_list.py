class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self, item):
        for i in self.items:
            if item.split()[1] in i:
                return self.items.remove(i)

    def show(self):
        values = []
        self.items = reversed(self.items)
        for tb in self.items:
            print(f'{tb[0]}: R$ {float(tb[1]):.2f}')
            values.append(float(tb[1]))
        print('----------------------')
        print(f'{len(values)} item(ns): R$ {float(sum(values)):.2f}')


shop = Stack()
while True:
    entry = input()
    if entry == 'fim':
        break
    elif '-' in entry:
        shop.pop(entry)
    else:
        shop.push(entry.split())

shop.show()
