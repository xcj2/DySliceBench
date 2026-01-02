# Binary search tree I 二分探索木：挿入


class Node():

    def __init__(self, k):
        self.k = k
        self.p = None
        self.l = None
        self.r = None
    
    def __repr__(self):
        return str(self.k)


def insert(z):
    if z == T[0]:
        return
    y = None
    x = T[0]
    while x != None:
        y = x 
        if z.k < y.k:
            x = y.l
        else:
            x = y.r
    z.p = y

    if z.k < y.k:
        y.l = z
    else:
        y.r = z


def find(k):
    x = T[0]
    while True:
        if x == None:
            return False
        elif x.k == k:
            return True
        elif x.k > k:
            x = ｘ.l
        elif x.k < k:
            x = x.r


def preparse(u):
    print(" ", u.k, sep="", end="")
    if u.l != None:
        preparse(u.l)
    if u.r != None:
        preparse(u.r)


def inparse(u):
    if u.l != None:
        inparse(u.l)
    print(" ", u.k, sep="", end="")
    if u.r != None:
        inparse(u.r)


m = int(input())
T = [None for i in range(m)]
for id in range(m):
    cmd = input().split()
    if cmd[0] == "insert":
        T[id] = Node(int(cmd[1]))
        insert(T[id])
    elif cmd[0] == "print":
        inparse(T[0])
        print()
        preparse(T[0])
        print()
    elif cmd[0] == "find":
        if find(int(cmd[1])):
            print("yes")
        else:
            print("no")

