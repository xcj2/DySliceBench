m = int(input())

class Node:
    def __init__(self, key, left ,right):
        self.key = key
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root
    def setRoot(self, v):
        self.root = v

    def inorder(self, v=None):
        if v is None:
            v = self.root
        if v.left is not None:
            self.inorder(v.left)
        print(' ' + str(v.key), end='')
        if v.right is not None:
            self.inorder(v.right)
        
    def preorder(self, v=None):
        if v is None:
            v = self.root
        print(' ' + str(v.key), end='')
        if v.left is not None:
            self.preorder(v.left)
        if v.right is not None:
            self.preorder(v.right)

def insert(T, z):
    y = None
    x = T.getRoot()
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y

    if y is None:
        T.setRoot(z)
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def find(T, k, noprint=False):
    x = T.getRoot()
    while x is not None:
        if x.key == k:
            if not noprint:
                print('yes')
            return x
        elif x.key < k:
            x = x.right
        else:
            x = x.left
    print('no')

def getNext(v):
    if v.right is not None:
        return getMinimum(v.right)  
    y = v.p
    while y is not None and v == y.right:
        v = y
        y = y.p
    return y

def getMinimum(v):
    while v.left is not None:
        v = v.left
    return v


    
def delete(T, z):
    if not z.left and not z.right:
        p = z.p
        if z.key < p.key:
            p.left = None
        else:
            p.right = None

    elif z.left and not z.right:
        p = z.p
        c = z.left
        if z.key > p.key:
            p.right = c
        else:
            p.left = c
        c.p = p
    elif not z.left and z.right:
        p = z.p
        c = z.right
        if z.key > p.key:
            p.right = c
        else:
            p.left = c
        c.p = p
    else:
        n = getNext(z)
        z.key = n.key
        delete(T, n)

T = BinaryTree()

for i in range(m):
    inp = input().split()
    if inp[0] == 'print':
        T.inorder()
        print()
        T.preorder()
        print()
    elif inp[0] == 'find':
        find(T, int(inp[1]))
    elif inp[0] == 'delete':
        delete(T, find(T, int(inp[1]),True))
    else:
        v = Node(int(inp[1]), None, None)
        insert(T, v)