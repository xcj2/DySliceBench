class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

def insert(z,root):
    y = None
    x = root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

    return root

def printPreorderList(p):
    if p == None:
        return
    print("",p.key,end = "")
    printPreorderList(p.left)
    printPreorderList(p.right)

def printInorderList(p):
    if p == None:
        return
    printInorderList(p.left)
    print("",p.key,end = "")
    printInorderList(p.right)

def find(key, root):
    x = root
    while x != None and key != x.key:
        if key < x.key:
            x = x.left
        else:
            x = x.right
    return x

def delete(key, root):
    z = find(key, root)
    if z == None:
        return root
    elif z.left == None and z.right == None: 
        if z.p.left == z:
            z.p.left = None
        else:
            z.p.right = None
        #z = None
    elif z.left != None and z.right == None:
        if z == root:
            root = z.left

        if z.p.left == z:
            z.p.left = z.left
        else:
            z.p.right = z.left
        z.left.p = z.p
        #z = None
    elif z.left == None and z.right != None:
        if z == root:
            root = z.right

        if z.p.left == z:
            z.p.left = z.right
        else:
            z.p.right = z.right
        z.right.p = z.p
        #z = None
    else:
        y = z.right
        while y.left != None:
            y = y.left
        z.key = y.key
        if y.right != None:
            y.right.p = y.p
        if y.p.left == y:
            y.p.left = None
        else:
            y.p.right = None
        #y = None

    return root

n = int(input())
root = None
for ni in range(n):
    s = input()
    if s[0] == "i":
        s, key = s.split()
        key = int(key)
        root = insert(Node(key), root)
    elif s[0] == "p":
        printInorderList(root)
        print()
        printPreorderList(root)
        print()
    elif s[0] == "f":
        s, key = s.split()
        key = int(key)
        ans = find(key, root)
        if ans == None:
            print("no")
        else:
            print("yes")
    elif s[0] == "d":
        s, key = s.split()
        key = int(key)
        root = delete(key, root)
