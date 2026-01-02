class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

def insert(T,z,root):
    y = None
    x = root
    T.append(z)
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

    return T, root

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
'''
def findRoot(T):
    if T == []:
        return None
    root = T[0].p
    while root != None:
        root = root.p
    return root
'''
n = int(input())
T=[]
root = None
for ni in range(n):
    s = input()
    if s[0] == "i":
        s, key = s.split()
        key = int(key)
        T, root = insert(T, Node(key), root)
    elif s[0] == "p":
        printInorderList(root)
        print()
        printPreorderList(root)
        print()
