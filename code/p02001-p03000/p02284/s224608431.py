class node:
    def __init__(self):
        self.p = -1
        self.l = -1
        self.r = -1

def preParse(u):
    if u == -1:
        return
    print(" " + str(u), end = '')
    preParse(T[u].l)
    preParse(T[u].r)

def inParse(u):
    if u == -1:
        return
    inParse(T[u].l)
    print(" " + str(u), end = '')
    inParse(T[u].r)

def postParse(u):
    if u == -1:
        return
    postParse(T[u].l)
    postParse(T[u].r)
    print(" " + str(u), end = '')

root = -1
def insert(T, z):
    global root
    parent = -1
    u = root
    while u != -1:
        parent = u
        if z < u:
            u = T[u].l
        else:
            u = T[u].r
    T[z].p = parent
    if parent == -1:
        root = z
    elif z < parent:
        T[parent].l = z
    else:
        T[parent].r = z

def find(T, k):
    u = root
    while u != -1 and k != u:
        if k < u:
            u = T[u].l
        else:
            u = T[u].r
    return "no" if u == -1 else "yes"

n = int(input())
cmdList = [input() for _ in range(n)]
T = {int(cmd[7:]): node() for cmd in cmdList if cmd[0] == "i"}

for cmd in cmdList:
    if cmd[0] == "p":
        inParse(root)
        print("")
        preParse(root)
        print("")
    elif cmd[0] == "f":
        print(find(T, int(cmd[5:])))
    else:
        insert(T, int(cmd[7:]))
