class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
    
class Tree():
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        
        node.parent = y
        if y is None:   # Tree が空だった場合
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
    
    def print_inorder_tree_walk(self):
        def work(node):
            if node is None:
                return
            work(node.left)
            print('', node.key, end='')
            work(node.right)

        work(self.root)
        print()
    
    def print_preorder_tree_walk(self):
        def work(node):
            if node is None:
                return
            print('', node.key, end='')
            work(node.left)
            work(node.right)

        work(self.root)
        print()


import sys

n = int(input())
T = Tree()
for _ in range(n):
    command, *args = sys.stdin.readline().split()
    if command[0] == 'i':   # insert key
        T.insert(Node(int(args[0])))
    else:   # print
        T.print_inorder_tree_walk()
        T.print_preorder_tree_walk()
