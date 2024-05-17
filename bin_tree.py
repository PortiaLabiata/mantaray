class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data
        self.l_height = self.r_height = 0

    def add(self, data):
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
                self.r_height = 1
            else:
                self.r_height = self.right.add(data)
            self.right_roll(self.right.l_height - self.right.r_height)

        elif data < self.data:
            if self.left is None:
                self.left = Node(data)
                self.l_height = 1
            else:
                self.l_height = self.left.add(data)
            self.left_roll(self.left.l_height - self.left.r_height)

        return max(self.r_height, self.l_height) + 1

    def right_roll(self, d):
        if d == 2:
            if self.right.left.l_height == self.r_height - 2:
                self.roll_llr()
            else:
                self.roll_blr()
        elif d == -2:
            if self.right.right.r_height == self.r_height - 2:
                self.roll_lrr()
            else:
                self.roll_brr()

    def left_roll(self, d):
        if d == 2:
            if self.left.left.l_height == self.l_height - 2:
                self.roll_lll()
            else:
                self.roll_bll()
        elif d == -2:
            if self.left.right.r_height == self.l_height - 2:
                self.roll_lrl()
            else:
                self.roll_brl()

    def roll_llr(self):
        a = self.right
        b = a.left
        self.right = b
        a.left = b.right
        b.right = a
        a.l_height = b.r_height
        b.r_height = a.l_height + 1
        self.r_height = a.l_height + 2

    def roll_blr(self):
        a = self.right
        b = a.left
        c = b.right
        self.right = c
        a.left = c.right
        a.l_height = c.r_height
        b.right = c.left
        b.r_height = c.l_height
        c.left = b
        c.right = a
        c.l_height = c.r_height = a.l_height + 1
        self.r_height -= 1

    def roll_lrr(self):
        a = self.right
        b = a.right
        self.right = b
        a.right = b.left
        b.left = a
        a.r_height = b.l_height
        b.l_height = a.r_height + 1
        self.r_height = a.r_height + 2

    def roll_brr(self):
        a = self.right
        b = a.right
        c = b.left
        self.right = c
        a.right = c.left
        a.r_height = c.l_height
        b.left = c.right
        b.l_height = c.r_height
        c.right = b
        c.left = a
        c.l_height = c.r_height = a.l_height + 1
        self.r_height -= 1

    def roll_lll(self):
        a = self.left
        b = a.left
        self.left = b
        a.left = b.right
        b.right = a
        a.l_height = b.r_height
        b.r_height = a.l_height + 1
        self.l_height = a.l_height + 2

    def roll_bll(self):
        a = self.left
        b = a.left
        c = b.right
        self.left = c
        a.left = c.right
        a.l_height = c.r_height
        b.right = c.left
        b.r_height = c.l_height
        c.left = b
        c.right = a
        c.l_height = c.r_height = a.l_height + 1
        self.l_height -= 1

    def roll_lrl(self):
        a = self.left
        b = a.right
        self.left = b
        a.right = b.left
        a.r_height = b.l_height
        b.left = a
        b.l_height = a.r_height + 1
        self.l_height = a.r_height + 2

    def roll_brl(self):
        a = self.left
        b = a.right
        c = b.left
        self.left = c
        a.right = c.left
        a.r_height = c.l_height
        b.left = c.right
        b.l_height = c.r_height
        c.right = b
        c.left = a
        c.l_height = c.r_height = a.l_height + 1
        self.l_height -= 1

    def __str__(self):
        return f'{"" if self.left is None else self.left} {self.data}{"" if self.right is None else self.right}'

    def __iter__(self):
        if self.left is not None:
            yield from self.left
        yield self.data
        if self.right is not None:
            yield from self.right

class BinTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.add(data)
        self.roll(self.root.l_height - self.root.r_height)

    def roll(self, d):
        if d == 2:
            if self.root.left.l_height == self.root.r_height + 1:
                self.roll_ll()
            else:
                self.roll_bl()
        elif d == -2:
            if self.root.right.r_height == self.root.l_height + 1:
                self.roll_lr()
            else:
                self.roll_br()

    def roll_ll(self):
        a = self.root
        b = a.left
        b.l_height = a.l_height
        self.root = b
        a.left = b.right
        a.l_height = b.r_height
        b.right = a
        b.r_height = a.l_height + 1

    def roll_bl(self):
        a = self.root
        b = a.left
        c = b.right
        self.root = c
        a.left = c.right
        a.l_height = c.r_height
        b.right = c.left
        b.r_height = c.l_height
        c.left = b
        c.right = a
        c.l_height = c.r_height = a.l_height + 1

    def roll_lr(self):
        a = self.root
        b = a.right
        self.root = b
        a.right = b.left
        a.r_height = b.l_height
        b.left = a
        b.l_height = a.r_height + 1

    def roll_br(self):
        a = self.root
        b = a.right
        c = b.left
        self.root = c
        a.right = c.left
        a.r_height = c.l_height
        b.left = c.right
        b.l_height = c.r_height
        c.right = b
        c.left = a
        c.l_height = c.r_height = a.l_height + 1

    def __str__(self):

        return str(self.root)


    def print_tree(self):
        from collections import deque
        h = 16
        d = deque()
        print(' ' * (h-1), end='')
        d.appendleft(self.root)
        d.appendleft('\n')
        d.appendleft(' ' * (h // 2 - 1))
        while len(d) > 2:
            n = d.pop()
            if type(n) is str:
                if n == '\n':
                    d.appendleft('\n')
                    h //= 2
                    d.appendleft(' ' * (h // 2 - 1))
                print(n, end='')
            elif n is not None:
                print(n.data, end='')
                d.appendleft(n.left)
                d.appendleft(' ' * (h - 1))
                d.appendleft(n.right)
                d.appendleft(' ' * (h - 1))
            else:
                print(' ', end='')
        print()

    def __iter__(self):
        if self.root is not None:
            yield from self.root

if __name__ == "__main__":
    from random import randint
    t = BinTree()
    print('\033[H\033[J', end='') # clear screen on linux
    for x in range(15):
        x = randint(10, 99)
        t.add(x)
        print('>', x)
        t.print_tree()
        input()
        print('\033[H\033[J', end='') # clear screen on linux

    t.print_tree()

    for x in t:
        print(x)

    print(t)
