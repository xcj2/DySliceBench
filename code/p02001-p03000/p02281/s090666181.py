class node:
    def __init__(self, parent, left, right):
        self.p = parent
        self.l = left
        self.r = right

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

n = int(input())
T = [node(-1, -1, -1) for _ in range(n)]
for _ in range(n):
    info = list(map(int, input().split(" ")))
    T[info[0]].l = info[1]
    T[info[0]].r = info[2]
    if info[1] != -1:
        T[info[1]].p = info[0]
    if info[2] != -1:
        T[info[2]].p = info[0]

print("Preorder")
for i in range(n):
    if T[i].p == -1:
        preParse(i)

print("\n" + "Inorder")
for i in range(n):
    if T[i].p == -1:
        inParse(i)

print("\n" + "Postorder")
for i in range(n):
    if T[i].p == -1:
        postParse(i)

print("")
