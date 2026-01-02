import sys


class Node:
    def __init__(self, key=None, pri=None):
        self.left = None
        self.right = None
        self.key = key
        self.pri = pri


def right_rotate(t: Node):
    s = t.left
    t.left = s.right
    s.right = t
    return s


def left_rotate(t: Node):
    s = t.right
    t.right = s.left
    s.left = t
    return s


def insert(t: Node, key: int, pri: int):
    if t is None:
        return Node(key, pri)
    if key == t.key:
        return t
    if key < t.key:
        t.left = insert(t.left, key, pri)
        if t.pri < t.left.pri:
            t = right_rotate(t)
    else:
        t.right = insert(t.right, key, pri)
        if t.pri < t.right.pri:
            t = left_rotate(t)
    return t


def erase(t: Node, key: int):
    if t is None:
        return None
    if key == t.key:
        if t.left is None and t.right is None:
            return None
        elif t.left is None:
            t = left_rotate(t)
        elif t.right is None:
            t = right_rotate(t)
        else:
            if t.left.pri > t.right.pri:
                t = right_rotate(t)
            else:
                t = left_rotate(t)
        return erase(t, key)
    if key < t.key:
        t.left = erase(t.left, key)
    else:
        t.right = erase(t.right, key)
    return t


def find(t: Node, x: int):
    while t is not None:
        if t.key == x:
            return 1
        elif t.key > x:
            t = t.left
        else:
            t = t.right
    return 0


def inorder(t: Node):
    if t.left is not None:
        inorder(t.left)
    print(" {}".format(t.key), end='')

    if t.right is not None:
        inorder(t.right)
    return


def preorder(t: Node):
    print(" {}".format(t.key), end='')

    if t.left is not None:
        preorder(t.left)
    if t.right is not None:
        preorder(t.right)
    return


def print_key(t: Node):
    inorder(t)
    print("\n", end='')
    preorder(t)
    print("\n", end='')
    return


line = sys.stdin.readline()
n = int(line)
root = None
for i in range(n):
    line = sys.stdin.readline().split()
    if line[0] == 'insert':
        k, p = int(line[1]), int(line[2])
        root = insert(root, k, p)
    elif line[0] == 'delete':
        k = int(line[1])
        root = erase(root, k)
    elif line[0] == 'find':
        k = int(line[1])
        if find(root, k):
            print("yes")
        else:
            print("no")
    else:
        print_key(root)

