# ALDS1_8_c Binary Search Tree III


# ALDS1_8_B Binary Search Tree II
import sys

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

    def find(self, num, node):
        if num < node.key:
            if node.left:
                self.find(num, node.left)
            else:
                print('no')
        elif num > node.key:
            if node.right:
                self.find(num, node.right)
            else:
                print('no')
        else:
            print('yes')
            return

    def find2del(self, num, node):
        if num < node.key:
            ans = self.find2del(num, node.left)
            return ans
        elif num > node.key:
            ans = self.find2del(num, node.right)
            return ans
        else:
            return node

    def successor(self, node):
        if node.right:
            nex = node.right
            while nex.left:
                nex = nex.left
            return nex

        nex = node.parent
        while nex & (nex.right == node):
            node = nex
            nex = nex.parent
        return nex

    def delete(self, num, node):
        # search the num in tree
        node_del = self.find2del(num, node)
        z = node_del
        if (node_del.left is not None) & (node_del.right is not None):
            node_del = self.successor(node_del)

        if node_del.left is not None:
            x = node_del.left
        else:
            x = node_del.right

        if x is not None:
            x.parent = node_del.parent

        if node_del.parent is None:
            self.root = x
        elif node_del.parent.left == node_del:
            node_del.parent.left = x
        else:
            node_del.parent.right = x

        if z != node_del:
            z.key = node_del.key

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
        if command == 'insert':
            tree.insert(num)
        elif command == 'find':
            tree.find(num, tree.root)
        else:
            tree.delete(num, tree.root)

