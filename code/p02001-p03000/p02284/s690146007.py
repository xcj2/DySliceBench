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
    while x != None:
        if key == x.key:
            print("yes")
            return
        elif key < x.key:
            x = x.left
        else:
            x = x.right
    print("no")


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
        find(key, root)
