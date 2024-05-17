from abc import ABC, abstractmethod

class AbstractList(ABC):

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def append(self, v):
        ...

    @abstractmethod
    def pop(self):
        ...

    @abstractmethod
    def __getitem__(self, index):
        ...

    @abstractmethod
    def __str__(self):
        ...

class LinkedList(AbstractList):

    def __init__(self):
        ...

    def append(self, v):
        ...

    def pop(self):
        ...

    def __getitem__(self, index):
        ...

    def __str__(self):
        ...

    @staticmethod
    def fuck():
        print('Fuck')

l = LinkedList()
LinkedList.fuck()
