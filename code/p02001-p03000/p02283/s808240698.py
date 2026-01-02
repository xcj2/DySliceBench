import sys


class Node:
    __slots__ = ['key', 'parent', 'left', 'right']

    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None


def insert(root, z):
    if root is None:
        return z

    y = None
    x = root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right

    z.parent = y

    if z.key < y.key:
        y.left = z
    else:
        y.right = z

    return root


def inorder(node):
    if not node:
        return
    yield from inorder(node.left)
    yield node.key
    yield from inorder(node.right)


def preorder(node):
    if not node:
        return
    yield node.key
    yield from preorder(node.left)
    yield from preorder(node.right)


def print_tree(root):
    print(''.join(' ' + str(key) for key in inorder(root)))
    print(''.join(' ' + str(key) for key in preorder(root)))


root = None

n = int(sys.stdin.readline())
for _ in range(n):
    command, *args = sys.stdin.readline().split()
    if command == 'insert':
        root = insert(root, Node(int(args[0])))
    else:
        print_tree(root)

