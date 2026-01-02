class BinarySearchTree:
    def __init__(self):
        self.root = None
    def show_keys(self):
        in_order_from(self.root)
        print('')
        pre_order_from(self.root)
        print('')
    def insert(self, key):
        node = Node(key)
        insert(self, node)
    def find(self, key):
        if find_from(self.root, key):
            print('yes')
        else:
            print('no')
    def delete_key(self, key):
        node = find_from(self.root, key)
        delete_node(self, node)

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

def delete_node(T, node):
    if node.left and node.right:
        x = node.right
        while x.left:
            x = x.left
        node.key = x.key
        delete_node(T, x)
    elif node.left or node.right:
        child = node.left or node.right
        if node is T.root:
            T.root = child
            child.parent = None
        else:
            if node.parent.left is node:
                node.parent.left = child
                child.parent = node.parent
            else:
                node.parent.right = child
                child.parent = node.parent
    else:
        if node.parent.left is node:
            node.parent.left = None
        else:
            node.parent.right = None

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

def find_from(node, k):
    while node:
        if node.key == k:
            return node
        if k < node.key:
            node = node.left
        else:
            node = node.right


import sys

t = BinarySearchTree()

m = sys.stdin.readline()

for i in sys.stdin.readlines():
    if i[0] == 'i':
        t.insert(int(i[7:]))
    elif i[0] == 'f':
        t.find(int(i[5:]))
    elif i[0] == 'd':
        t.delete_key(int(i[7:]))
    else:
        t.show_keys()

