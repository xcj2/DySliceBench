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

def preOrder(x):
    if x == None:
        return
    global preList
    preList.append(x.key)
    
    preOrder(x.l)
    preOrder(x.r)

def inOrder(x):
    if x == None:
        return
    inOrder(x.l)

    global inList
    inList.append(x.key)
    
    inOrder(x.r)

def Find(x,z):
    while x != None and z.key != x.key:
        y = x
        if z.key < x.key:
            x = x.l
        else:
            x = x.r
    return x


def Delete(x, z):
    if z.l == None or z.r == None:
        y = z
    else:
        y = getSuccessor(z)

    if y.l != None:
        x = y.l
    else:
        x = y.r

    if x != None:
        x.p = y.p

    if y.p == None:
        pass
    elif y == y.p.l:
        y.p.l = x
    else:
        y.p.r = x
    if y != z:
        z.key = y.key
        
def getSuccessor(x):
    if x.r != None:
        return getMinimum(x.r)
    y = x.p
    while y != None and x == y.r:
        x = y
        y = y.p
    return y

def getMinimum(x):
    while x.l != None:
        x = x.l
    return x

root = None
for data in trees:
    if data[0] == "print":
        inList = []
        preList = []
        inOrder(root)
        a = " " + " ".join([str(num) for num in inList])
        print(a)

        preOrder(root)
        a = " " + " ".join([str(num) for num in preList])
        print(a)

    else:
        z = BinaryTree(int(data[1]))
        if data[0] == "insert":
            root = Insert(root,z)
        elif data[0] == "find":
            a = Find(root, z)
            if a == None:
                print("no")
            else:
                print("yes")
        elif data[0] == "delete":
            Delete(root, Find(root,z))
  

