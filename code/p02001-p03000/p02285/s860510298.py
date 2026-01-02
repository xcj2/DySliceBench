import sys


class Node:
    __slots__ = ['key', 'parent', 'left', 'right']

    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def replace(self, child, new_child):
        if child is self.left:
            self.left = new_child
        else:
            self.right = new_child
        if new_child:
            new_child.parent = self

    def __str__(self):
        return f'({str(self.left or "_")} {self.key} {str(self.right or "_")})'


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


def find(node, key):
    while node and node.key != key:
        if key < node.key:
            node = node.left
        elif key > node.key:
            node = node.right
    return node


def next_node(node):
    while node.left:
        node = node.left
    return node


def delete(root, key):
    node = find(root, key)
    if not node:
        return root
    if node is root:
        return None

    delete_node(node)
    return root


def delete_node(node):
    if not node.left and not node.right:
        node.parent.replace(node, None)
    elif node.left and node.right:
        next = next_node(node.right)
        node.key = next.key
        delete_node(next)
    else:  # node.left xor node.right
        node.parent.replace(node, node.left or node.right)


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
    elif command == 'find':
        print('yes' if find(root, int(args[0])) else 'no')
    elif command == 'delete':
        root = delete(root, int(args[0]))
    else:
        print_tree(root)

