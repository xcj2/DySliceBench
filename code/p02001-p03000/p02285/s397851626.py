class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


root = None

def insert(k):
    global root
    y = None
    x = root
    z = Node(k)

    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right

    z.parent = y
    if y is None:
        root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z


def find(u, k):
    while u is not None and k != u.key:
        if k < u.key:
            u = u.left
        else:
            u = u.right
    return u


def treeMinimum(x):
    while x.left is not None:
        x = x.left
    return x


def treeSuccessor(x):
    if x.right is not None:
        return treeMinimum(x.right)
    y = x.parent
    while y is not None and x == y.right:
        x = y
        y = y.parent
    return y


def treeDelete(z):
    if z is None:
        return

    global root
    if z.left is None or z.right is None:
        y = z
    else:
        y = treeSuccessor(z)

    if y.left is not None:
        x = y.left
    else:
        x = y.right

    if x is not None:
        x.parent = y.parent

    if y.parent is None:
        root = x
    else:
        if y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

    if y != z:
        z.key = y.key


def inorder(u):
    if u is None:
        return
    inorder(u.left)
    print(' %d' % u.key, end='')
    inorder(u.right)


def preorder(u):
    if u is None:
        return
    print(' %d' % u.key, end='')
    preorder(u.left)
    preorder(u.right)


n = int(input())
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'insert':
        insert(int(cmd[1]))
    elif cmd[0] == 'find':
        if find(root, int(cmd[1])) is not None:
            print('yes')
        else:
            print('no')
    elif cmd[0] == 'delete':
        treeDelete(find(root, int(cmd[1])))
    elif cmd[0] == 'print':
        inorder(root)
        print()
        preorder(root)
        print()
