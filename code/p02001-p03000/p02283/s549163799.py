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
    else:
        inParse(root)
        preParse(root)

        print(" " + " ".join([str(i) for i in inParseList]))
        print(" " + " ".join([str(i) for i in preParseList]))
        preParseList = []
        inParseList = []

