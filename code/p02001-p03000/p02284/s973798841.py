# Binary search trees - Binary Search Tree II
class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def find(self, key):
        return self._find(key, self.root)

    def _find(self, key, nd):
        if not nd: return False
        if nd.key == key: return True
        if key < nd.key:
            return self._find(key, nd.left)
        else:
            return self._find(key, nd.right)
    
    def printorder(self):
        self._preorder_walk(self.root)
        print()
        self._inorder_walk(self.root)
        print()

    def _inorder_walk(self, nd):
        print(' {0}'.format(nd.key), end='')
        if nd.left: self._inorder_walk(nd.left)
        if nd.right: self._inorder_walk(nd.right)

    def _preorder_walk(self, nd):
        if nd.left: self._preorder_walk(nd.left)
        print(' {0}'.format(nd.key), end='')
        if nd.right: self._preorder_walk(nd.right)

class Node:
    def num_child(self):
        d = 1 if self.left else 0
        d += 1 if self.right else 0
        return d
    def __init__(self, key):
        self.key = key
        self.right,self.left = None,None
        self.parent = None
    def __str__(self):
        return 'node key: ' + str(self.key)

def insert(T, z):
    y = None
    x = T.root
    while not x == None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if z.parent == None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    T.size += 1

m = int(input())
T = Tree()
for _ in range(m):
    ss = input().split()
    op = ss[0]
    if op == 'insert':
        v = int(ss[1])
        insert(T, Node(v))
    elif op == 'print':
        T.printorder()
    elif op == 'find':
        v = int(ss[1])
        if T.find(v): print('yes')
        else: print('no')
