class Heap(object):

    def __init__(self):
        self.array = []

    def put(self, v):
        self.array.append(v)
        i = len(self.array) - 1
        self.sift_up(i)

    def pop(self):
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        aux = self.array.pop()
        self.sift_down(0)
        return aux

    def sift_up(self, i):
        while i > 0 and self.array[i] < self.array[(i - 1) // 2]:
            j = (i - 1) // 2
            self.array[i], self.array[j] = self.array[j], self.array[i]
            i = j

    def sift_down(self, i):
        while 2*i + 1 < len(self.array):
            left = 2*i + 1
            right = 2*i + 2
            j = left
            if right < len(self.array) and self.array[right] < self.array[left]:
                j = right
            if self.array[i] <= self.array[j]:
                break
            self.array[i], self.array[j] = self.array[j], self.array[i]
            i = j

    def build_heap(self, a):
        self.array = a[:]
        for i in range(len(self) // 2, -1, -1):
            self.sift_down(i)

    def __str__(self):
        return str(self.array)

    def __len__(self):
        return len(self.array)

h = Heap()
h.build_heap([7, 6, 5, 4, 3, 2, 0])
print(h)
