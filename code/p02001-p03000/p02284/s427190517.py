class BinarySearchTree:
    def __init__(self):
        self.root = None
    def in_order_traversal(self):
        in_order_from(self.root)
        print('')
    def pre_order_traversal(self):
        pre_order_from(self.root)
        print('')
    def insert(self, key):
        node = Node(key)
        insert(self, node)
    def find(self, key):
        if find(self.root, key):
            print('yes')
        else:
            print('no')

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

def in_order_from(node):
    if node:
        in_order_from(node.left)
        print(' {0}'.format(node.key), end = '')
        in_order_from(node.right)

def pre_order_from(node):
    if node:
        print(' {0}'.format(node.key), end = '')
        pre_order_from(node.left)
        pre_order_from(node.right)

def find(node, k):
    while node:
        if node.key == k:
            return True
        if k < node.key:
            node = node.left
        else:
            node = node.right
    return False


import sys

t = BinarySearchTree()

m = sys.stdin.readline()

for i in sys.stdin.readlines():
    if i[0] == 'i':
        t.insert(int(i[7:]))
    elif i[0] == 'f':
        t.find(int(i[5:]))
    else:
        t.in_order_traversal()
        t.pre_order_traversal()