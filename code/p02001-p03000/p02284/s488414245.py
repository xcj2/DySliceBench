import sys
readline = sys.stdin.readline
class Node:
    __slots__ = ['value', 'left', 'right']
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
class BinTree:
    __slots__ = ['_tree', 'result']
    def __init__(self):
        self._tree = None
    def insert(self, value):
        p = None
        c = self._tree
        while c is not None:
            p = c
            if value < c.value:
                c = c.left
            else:
                c = c.right
        if p is None:
            self._tree = Node(value)
        elif value < p.value:
            p.left = Node(value)
        else:
            p.right = Node(value)
    def find(self, value):
        c = self._tree
        while c is not None:
            if value == c.value:
                return True
            elif value < c.value:
                c = c.left
            else:
                c = c.right
        return False
    def preoder_walk(self):
        self.result = []
        def preoder(node):
            if node is not None:
                self.result.append(node.value)
                preoder(node.left)
                preoder(node.right)
        preoder(self._tree)
        print(" " + " ".join(map(str, self.result)))
    def inorder_walk(self):
        self.result = []
        def inorder(node):
            if node is not None:
                inorder(node.left)
                self.result.append(node.value)
                inorder(node.right)
        inorder(self._tree)
        print(" " + " ".join(map(str, self.result)))
n = int(input())
tree = BinTree()
for _ in range(n):
    com = readline().split()
    if com[0] == "insert":
        tree.insert(int(com[1]))
    elif com[0] == "find":
        print("yes" if tree.find(int(com[1])) else "no")
    else:
        tree.inorder_walk()
        tree.preoder_walk()

