class node:
    def __init__(self, key):
        self.k = key
        self.p = None
        self.l = None
        self.r = None

def preParse(u):
    if u == None:
        return
    print(" " + str(u.k), end = '')
    preParse(u.l)
    preParse(u.r)

def inParse(u):
    if u == None:
        return
    inParse(u.l)
    print(" " + str(u.k), end = '')
    inParse(u.r)

def postParse(u):
    if u == None:
        return
    postParse(u.l)
    postParse(u.r)
    print(" " + str(u.k), end = '')

root = None
def insert(k):
    global root
    parent = None
    u = root
    z = node(k)
    while u != None:
        parent = u
        if z.k < u.k:
            u = u.l
        else:
            u = u.r

    z.p = parent
    if parent == None:
        root = z
    elif z.k < parent.k:
        parent.l = z
    else:
        parent.r = z

def find(k):
    global root
    u = root
    while u != None and u.k != k:
        if k < u.k:
            u = u.l
        else:
            u = u.r
    return u

def delete (k):
    global root
    u = find(k)
    if u.l == None or u.r == None:
        y = u
    else:
        y = getSuccessor(u)

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

    if y != u:
        u.k = y.k

def getSuccessor(z):
    if z.r != None:
        return getMinimum(z.r)
    
    y = z.p
    while y != None and z == y.r:
        z = y
        y = y.p
    return y

def getMinimum(z):
    while z.l != None:
        z = z.l
    return z

n = int(input())
cmdList = [input() for _ in range(n)]

for cmd in cmdList:
    if cmd[0] == "p":
        inParse(root)
        print("")
        preParse(root)
        print("")
    elif cmd[0] == "f":
        print("no" if find(int(cmd[5:])) == None else "yes")
    elif cmd[0] == "d":
        a = 1
        delete(int(cmd[7:]))
    else:
        insert(int(cmd[7:]))
