#coding:utf-8

class MakeTree():
    def __init__(self, key, p=None, l=None, r=None):
        self.key = key
        self.p = p
        self.l = l
        self.r = r

 
def Insert(root,value):
    y = None
    x = root
    z = MakeTree(value)

    while x != None:
        y = x
        if x.key > z.key:
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


def Find(u, target):
    y = None
    x = u
    while x != None and target != x.key:
        y = x
        if x.key > target:
            x = x.l
        else:
            x = x.r
    return x


def Delete(u, z):
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
        root = x
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


def inParse(u):
    if u == None:
        return
    inParse(u.l)
    global inParseList
    inParseList.append(u.key)
    inParse(u.r)

def preParse(u):
    if u == None:
        return
    global preParseList
    preParseList.append(u.key)
    preParse(u.l)
    preParse(u.r)


root = None       
n = int(input())
inParseList = []
preParseList = []
for i in range(n):
    order = list(input().split())
    if order[0] == "insert":
        root = Insert(root, int(order[1]))
        
    elif order[0] == "print":
        inParse(root)
        preParse(root)
        print(" " + " ".join([str(i) for i in inParseList]))
        print(" " + " ".join([str(i) for i in preParseList]))
        preParseList = []
        inParseList = []
        
    elif order[0] == "find":
        x = Find(root, int(order[1]))
        if x == None:
            print("no")
        else:
            print("yes")
    else:
        x = Find(root, int(order[1]))
        Delete(root, x)






        

