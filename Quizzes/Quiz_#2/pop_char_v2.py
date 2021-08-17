class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


command = input()
s = Queue()
new_string = ''
for letter in command:
    if letter != '*':
        s.enqueue(letter)
    else:
        new_string += s.dequeue()

print(new_string)
