class Stack:
    def __init__(self):
        self.items = []

    def push(self, typee, color, qtd):
        self.items.append((typee, color, qtd))

    def isEmpthy(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def stack(self):
        return self.items

    def show(self):
        last = self.items.pop()
        return f'Tipo: {last[0]}, Cor: {last[1]}'


s = Stack()
n = int(input())

for i in range(n):
    cloth, color, qtd = input().split()
    s.push(cloth, color, qtd)
size = s.size()
time = 0
for j in s.stack():
    time += int(j[-1])

while not s.isEmpthy():
    print(s.show())
print(f'Total de roupas: {size}')
print(f'Total de tempo: {time}')
