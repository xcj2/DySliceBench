class Node:
    def __init__(self):
        self.key = -1
        self.p = -1
        self.l = -1
        self.r = -1

def insert(k):
    y = -1
    x = root[0]
    z = len(T)
    T.append(Node())
    T[z].key = k
    while x != -1:
        y = x
        if T[z].key < T[x].key: x = T[x].l
        else: x = T[x].r
    T[z].p = y
    if y == -1: root[0] = z
    elif T[z].key < T[y].key: T[y].l = z
    else: T[y].r = z

def inorder(u):
    if u == -1: return
    inorder(T[u].l)
    print(" {}".format(T[u].key),end="")
    inorder(T[u].r)

def preorder(u):
    if u == -1: return
    print(" {}".format(T[u].key),end="")
    preorder(T[u].l)
    preorder(T[u].r)

m = int(input())
T = []
root = [-1]
for _ in range(m):
    comm = input().split()
    if comm[0] == "insert":
        insert(int(comm[1]))
    else:
        inorder(root[0])
        print("")
        preorder(root[0])
        print("")
