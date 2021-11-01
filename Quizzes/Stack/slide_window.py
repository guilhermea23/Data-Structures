class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addRear(self, item):
        self.items.insert(0, item)

    def addFront(self, item):
        self.items.append(item)

    def removeRear(self):
        return self.items.pop(0)

    def removeFront(self):
        return self.items.pop()

    def show(self):
        return self.items


deque = Deque()
n = int(input())
elements = input().split()
k = int(input())

for i in elements:
    deque.addFront(int(i))

new_string = ''
while not deque.isEmpty():
    bigger = str(max(deque.show()[:k]))
    new_string += bigger
    deque.removeRear()
    if deque.size() < k:
        break
print(*new_string)
