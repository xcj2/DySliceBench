# Binary Search Tree 1

import sys
sys.setrecursionlimit(10**6)


class Node():
    __slots__ = ['key', 'parent', 'left', 'right']
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        k = str(self.key)
        p = str(self.parent.key) if self.parent else 'None'
        l = str(self.left.key) if self.left else 'None'
        r = str(self.right.key) if self.right else 'None'
        s = "<Node %s: parent=%s, left=%s, right=%s>" % (k, p, l, r)
        return s


class BinaryTree():
    def __init__(self, n=0):
        self.T = [Node() for _ in range(n)]
        self.root = None

    def preorder(self):
        self.preorder_key = []
        self.preorder_rec(self.root)
        print('', *(self.preorder_key))

    def preorder_rec(self, node):
        if node == None:
            return
        self.preorder_key.append(node.key)
        self.preorder_rec(node.left)
        self.preorder_rec(node.right)

    def inorder(self):
        self.inorder_key = []
        self.inorder_rec(self.root)
        print('', *(self.inorder_key))

    def inorder_rec(self, node):
        if node == None:
            return
        self.inorder_rec(node.left)
        self.inorder_key.append(node.key)
        self.inorder_rec(node.right)

    def insert(self, key):
        node = Node(key)

        y = None
        x = self.root

        while x != None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif key < y.key:
            y.left = node
        else:
            y.right = node


N = int(input())
S = [input() for _ in range(N)]
tree = BinaryTree()

for s in S:
    if 'print' in s:
        tree.inorder()
        tree.preorder()
    else:
        _, key = s.split()
        tree.insert(int(key))

