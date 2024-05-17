class Node(object):

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BST(object):

    def __init__(self):
        self.root = None

    def put(self, k):
        if self.root is None:
            self.root = Node(k)
        else:
            node = self.root
            while True:
                if k > node.value:
                    if node.right is None:
                        node.right = Node(k)
                        break
                    else:
                        node = node.right
                else:
                    if node.left is None:
                        node.left = Node(k)
                        break
                    else:
                        node = node.left

    def search(self, k):
        node = self.root
        while node is not None:
            if k == node.value:
                return True
            elif k <= node.value:
                node = node.left
            elif k > node.value:
                node = node.right
        return False


t = BST()
t.put(20)
t.put(10)
print(t.search(500))
