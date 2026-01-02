import sys
readline = sys.stdin.readline
from copy import deepcopy, copy
class Node:
    __slots__ = ['value', 'left', 'right']
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
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
    def delete(self, value):
        parent = None
        current = self._tree
        while current.value != value:
            parent = current
            if current is None:
                return
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        if current.left is None and current.right is None:
            if parent.left is current:
                parent.left = None
            else:
                parent.right = None
        elif current.left is None:
            if parent.left is current:
                parent.left = current.right
            else:
                parent.right = current.right
        elif current.right is None:
            if parent.left is current:
                parent.left = current.left
            else:
                parent.right = current.left
        else:
            next_node_parent = current
            next_node = current.right
            while next_node.left is not None:
                next_node_parent = next_node
                next_node = next_node.left
            if next_node.right is None:
                if next_node_parent.left is next_node:
                    next_node_parent.left = None
                else:
                    next_node_parent.right = None
            else:
                if next_node_parent.left is next_node:
                    next_node_parent.left = next_node.right
                else:
                    next_node_parent.right = next_node.right
            current.value = next_node.value
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
    elif com[0] == "delete":
        tree.delete(int(com[1]))
    else:
        tree.inorder_walk()
        tree.preoder_walk()

