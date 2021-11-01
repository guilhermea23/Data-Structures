class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self,elem):
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size +=1

    def __len__(self):
        return self._size

    def get(self,index):
        pass

    def set(self,index,elem):
        pass

    def __setItem__(self,index,elem):
        pointer = self.head
        for i in range(index):
             if pointer:
                 pointer = pointer.next
             else:
                 raise IndexError("list out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError('list out of range')

    def __getItem__(self,index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list out of range")
        if pointer:
            pointer.next
        else:
            raise IndexError('list out of range')
