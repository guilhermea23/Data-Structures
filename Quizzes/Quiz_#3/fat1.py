
from math import factorial


class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def popLeft(self):
        self.items.pop(0)

    def show(self):
        return self.items

    def size(self):
        return len(self.items)


numbers = Stack()
qtd = int(input("Insira quantos n's vc deseja calcular: "))


for i in range(qtd):
    n = int(input(f"Insira o {i+1}º número: "))
    numbers.push(n)


j = 0
factorials = []


while not numbers.isEmpty():
    for i in range(numbers.show()[0]+1):
        factorials.append(factorial(i))
    print(*factorials)
    factorials.clear()
    numbers.popLeft()
