class Node:
    def __init__(self, key, pri):
        self.key = key
        self.pri = pri
        self.left  = None
        self.right = None


def rightRotate(t):
    s = t.left
    t.left = s.right
    s.right = t
    return s

def leftRotate(t):
    s = t.right
    t.right = s.left
    s.left = t
    return s

def insert(t, key, pri):
    if t == None:
        return Node(key, pri)

    if key == t.key:
        return t

    if key < t.key:
        t.left = insert(t.left, key, pri)
        if t.pri < t.left.pri:
            t = rightRotate(t)
    else:
        t.right = insert(t.right, key, pri)
        if t.pri < t.right.pri:
            t = leftRotate(t)

    return t


def delete(t, key):
    if   t == None:
        return None

    if   key < t.key:
        t.left  = delete(t.left , key)
    elif key > t.key:
        t.right = delete(t.right, key)
    else:
        return _delete(t, key)
    return t


def _delete(t, key):
    if t.left == None and t.right == None:
        return None
    elif t.left  == None:
        t = leftRotate(t)
    elif t.right == None:
        t = rightRotate(t)
    else:
        if t.left.pri > t.right.pri:
            t = rightRotate(t)
        else:
            t = leftRotate(t)
    return delete(t, key)


def find(t, key):
    if t == None:
        return False

    if key == t.key:
        return True

    if key < t.key:
        return find(t.left, key)
    else:
        return find(t.right, key)

def priorder(t):
    if t == None:
        return

    print(' ' + str(t.key), end='')
    priorder(t.left)
    priorder(t.right)

def inorder(t):
    if t == None:
        return

    inorder(t.left)
    print(' ' + str(t.key), end='')
    inorder(t.right)


m = int(input())
t = None

for _ in range(m):
    com = input().split()

    if com[0] == 'insert':
        t = insert(t, int(com[1]), int(com[2]))
    elif com[0] == 'find':
        if find(t, int(com[1])):
            print('yes')
        else :
            print('no')
    elif com[0] == 'delete':
        t = delete(t, int(com[1]))
    elif com[0] == 'print':
        inorder(t)
        print()
        priorder(t)
        print()

