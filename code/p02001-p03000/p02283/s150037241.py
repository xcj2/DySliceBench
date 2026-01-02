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
    elif cmd[0] == 'print':
        inorder(root)
        print()
        preorder(root)
        print()
