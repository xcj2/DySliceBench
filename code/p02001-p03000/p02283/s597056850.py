#coding:utf-8
N = int(input())
trees = [list(input().split()) for i in range(N)]

class BinaryTree:
    def __init__(self,key,p=None,l=None,r=None):
        self.key = key
        self.p = p
        self.l = l
        self.r = r

def Insert(root,z):
    y = None
    x = root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.l
        else:
            x = x.r
    z.p = y

    if y == None:
        root = z
    elif z.key < y.key:
        y.l = z
    else:
        y.r = z
    return root

def preOrder(root):
    x = root
    if x == None:
        return
    global preList
    preList.append(x.key)
    
    preOrder(x.l)
    preOrder(x.r)

def inOrder(root):
    x = root
    if x == None:
        return
    inOrder(x.l)

    global inList
    inList.append(x.key)
    
    inOrder(x.r)

root = None
for data in trees:
    if data[0] == "insert":
        z = BinaryTree(int(data[1]))
        root = Insert(root,z)
    if data[0] == "print":
        inList = []
        preList = []
        inOrder(root)
        a = " " + " ".join([str(num) for num in inList])
        print(a)

        preOrder(root)
        a = " " + " ".join([str(num) for num in preList])
        print(a)

