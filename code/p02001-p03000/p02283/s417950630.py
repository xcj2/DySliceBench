class BinarySearchTree:
    def __init__(self):
        self.root = None
    def in_order_traversal(self):
        def _in_order_line(node):
            if node:
                _in_order_line(node.left)
                print(' {0}'.format(node.key), end = '')
                _in_order_line(node.right)
        _in_order_line(self.root)
        print('')
    def pre_order_traversal(self):
        def _pre_order_line(node):
            if node:
                print(' {0}'.format(node.key), end = '')
                _pre_order_line(node.left)
                _pre_order_line(node.right)
        _pre_order_line(self.root)
        print('')


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        

def insert(T, z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z



import sys

t = BinarySearchTree()

m = sys.stdin.readline()

for i in sys.stdin.readlines():
    if i[0] == 'i':
        k = int(i[7:])
        n = Node(k)
        insert(t, n)
    else:
        t.in_order_traversal()
        t.pre_order_traversal()