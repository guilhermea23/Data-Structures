class Elements:
    def __init__(self):
        self.items = []

    def ext(self, item):
        self.items.extend(item)

    def media(self):
        return sum(self.items)*(1/len(self.items))

    def size(self):
        return len(self.items)


cases = Elements()
n, m = input().split()
qtd = [int(x) for x in input().split()]
if len(qtd):
    cases.ext(qtd)

for i in range()
