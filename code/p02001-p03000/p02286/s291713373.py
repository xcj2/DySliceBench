class Node:
    def __init__(self, key=None, pri=None, left=None, right=None):
        self.key = key
        self.pri = pri
        self.left = left
        self.right = right
        self.parent = None

def rRotate(t):
    s = t.left
    t.left = s.right
    s.right = t
    return s

def lRotate(t):
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
            t = rRotate(t)
    else:
        t.right = insert(t.right, key, pri)
        if t.pri < t.right.pri:
            t = lRotate(t)

    return t

def find(x, k):
    while x != None and k != x.key:
        if x.key != None:
            if k < x.key:
                x = x.left
            else:
                x = x.right
    return x

def delete(t, key):
    if t == None:
        return None
    if key < t.key:
        t.left = delete(t.left, key)
    elif key > t.key:
        t.right = delete(t.right, key)
    else:
        if t.left == None and t.right == None:
            return None
        elif t.left == None:
            t = lRotate(t)
        elif t.right == None:
            t = rRotate(t)
        else:
            if t.left.pri > t.right.pri:
                t = rRotate(t)
            else:
                t = lRotate(t)
        return delete(t, key)
    return t

def inorder(u):
    if u == None:
        return
    inorder(u.left)
    print(' ' + str(u.key), end="")
    inorder(u.right)

def preorder(u):
    if u == None:
        return
    print(' ' + str(u.key), end="")
    preorder(u.left)
    preorder(u.right)

count = int(input())
t = None
for i in range(count):
    a = input().split()
    if a[0] == 'insert':
        t = insert(t, int(a[1]), int(a[2]))
    elif a[0] == 'find':
        if find(t, int(a[1])) == None:
            print('no')
        else:
            print('yes')
    elif a[0] == 'delete':
        t = delete(t, int(a[1]))
    else:
        inorder(t)
        print('\n', end="")
        preorder(t)
        print('\n', end="")

