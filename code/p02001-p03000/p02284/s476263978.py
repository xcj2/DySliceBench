import sys
readline = sys.stdin.readline
class Node:
    __slots__ = ['value', 'left', 'right']
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
class BinTree:
    def __init__(self):
        self._tree = None
        self._node_list = set()
    def insert(self, value):
        self._node_list.add(value)
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
        print("yes" if value in self._node_list else "no")
    def preoder_walk(self):
        def preoder(node):
            result = []
            if node is not None:
                result.extend([node.value])
            if node.left is not None:
                result.extend(preoder(node.left))
            if node.right is not None:
                result.extend(preoder(node.right))
            return result
        return preoder(self._tree)
    def inorder_walk(self):
        def inorder(node):
            result = []
            if node is not None:
                result.extend(inorder(node.left))
                result.append(node.value)
                result.extend(inorder(node.right))
            return result
        return inorder(self._tree)
n = int(input())
tree = BinTree()
for _ in range(n):
    com = readline().split()
    if com[0] == "insert":
        tree.insert(int(com[1]))
    elif com[0] == "find":
        tree.find(int(com[1]))
    else:
        print(" " + " ".join(map(str, tree.inorder_walk())))
        print(" " + " ".join(map(str, tree.preoder_walk())))

