# ALDS1_8_A Binary Search Tree 1
import sys


class Node:
    def __init__(self, x):
        self.parent = None
        self.left = None
        self.right = None
        self.key = x


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        new = Node(x)
        x_parent = self.root
        next = self.root

        while next is not None:
            x_parent = next
            if x < x_parent.key:
                next = x_parent.left
            else:
                next = x_parent.right

        if x_parent is None:
            self.root = new
        elif x < x_parent.key:
            new.parent = x_parent
            x_parent.left = new
        else:
            new.parent = x_parent
            x_parent.right = new
        return

    def preorder(self, node):
        print(' {}'.format(node.key), end='')

        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)
        return

    def inorder(self, node):
        if node.left:
            self.inorder(node.left)

        print(' {}'.format(node.key), end='')

        if node.right:
            self.inorder(node.right)


m = int(input())
tree = Tree()

for i in range(m):
    command = list(sys.stdin.readline().strip().split())
    if command[0] == 'print':
        tree.inorder(tree.root)
        print()
        tree.preorder(tree.root)
        print()
    else:
        num = command[1]
        command = command[0]
        num = int(num)
        tree.insert(num)


