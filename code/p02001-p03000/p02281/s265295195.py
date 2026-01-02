class Node:
    def __init__(self):
        self.p = -1
        self.l = -1
        self.r = -1

n = int(input())
T = [Node() for _ in range(n)]
for _ in range(n):
    i,l,r = map(int,input().split())
    T[i].l = l
    T[i].r = r
    if l != -1: T[l].p = i
    if r != -1: T[r].p = i

preorder = []
inorder = []
postorder = []

def preParse(u):
    if u == -1: return
    preorder.append(u)
    preParse(T[u].l)
    preParse(T[u].r)

def inParse(u):
    if u == -1: return
    inParse(T[u].l)
    inorder.append(u)
    inParse(T[u].r)

def postParse(u):
    if u == -1: return
    postParse(T[u].l)
    postParse(T[u].r)
    postorder.append(u)

r = 0
while T[r].p != -1: r += 1
preParse(r)
inParse(r)
postParse(r)

print("Preorder",end="\n ")
print(*preorder)
print("Inorder",end="\n ")
print(*inorder)
print("Postorder",end="\n ")
print(*postorder)
