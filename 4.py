from random import randint

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return 'Node: ' + str(self.value)

class LinkedList(object):

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def append(self, value):
        if self.length == 0:
            node = Node(value)
            self.first = node
            self.last = node
        else:
            self.last.next = Node(value)
            self.last = self.last.next
        self.length += 1

    def pop(self):
        aux = self.last.value
        node = self.first
        if self.length == 1:
            self.last = None
            self.first = None
            self.length -= 1
            return aux
        while node.next is not self.last:
            node = node.next
        self.last = node
        self.last.next = None
        self.length -= 1
        return aux

    def __str__(self):
        res = ''
        node = self.first
        while node is not None:
            res += f'{node.value}, '
            node = node.next
        return res

    def __len__(self):
        return self.length

l = LinkedList()
for _ in range(0, 10):
    v = randint(0, 100)
    l.append(v)
    print(l)

while len(l) > 0:
    l.pop()
    print(l)
