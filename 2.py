import string, random
from random import randint

class ClosedHashTable(object):

    def __init__(self, m=100):
        self.m = m
        self.table = [[] for _ in range(0, self.m)]

    def _hash(self, k):
        return hash(k) % self.m

    def put(self, k, v):
        h = self._hash(k)
        self.table[h].append((k, v))

    def get(self, k):
        h = self._hash(k)
        for key, value in self.table[h]:
            if key == k:
                return v
        return None

    def remove(self, k):
        h = self._hash(k)
        for index, (key, value) in enumerate(self.table[h]):
            if key == k:
                self.table[h].pop(index)

    def __str__(self):
        return ' '.join([str(l) if l != [] else '' for l in self.table])

class OpenHashTable(object):

    def __init__(self, m=100):
        self.m = m
        self.table = [None for _ in range(0, self.m)]
        self.taken = 0

    def _hash(self, k):
        return hash(k) % self.m

    def put(self, k, v):
        h = self._hash(k)
        while self.table[h] is not None:
            h += 1
        self.table[h] = (k, v)
        self.taken += 1

    def get(self, k):
        h = self._hash(k)
        while h < self.m and self.table[h] is not None and self.table[h][0] != k:
            h += 1
        if self.table[h] is None:
            return None
        else:
            return self.table[h][1]

    def remove(self, k):
        h = self._hash(k)
        while self.table[h][0] != k:
            if self.table[h] is None:
                return None
            h += 1
        self.table[h] = None

        empty = h
        h += 1
        while self.table[h] is not None:
            key, value = self.table[h]
            if key != self._hash(key):
                self.table[empty] = (key, value)
                self.table[h] = None
                empty = h
            h += 1

    def __str__(self):
        return str(self.table)

t = OpenHashTable()
k = None
for i in range(0, 70):
    k = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    t.put(k, i)
print(k)
print(t)
t.remove(k)
print(t)
