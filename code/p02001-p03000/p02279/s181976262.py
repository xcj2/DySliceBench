import sys
sys.setrecursionlimit(2**20)
n = int(input())
NIL = -1
class node:
    def __init__(self,parent,left,right):
        self.parent = parent
        self.left = left
        self.right = right
T = [node(NIL,NIL,NIL) for _ in range(n)]
firstid = 0
for _ in range(n):#入力の一例
    A = list(map(int,input().split()))
    id = A[0]
    if n == 1:
        firstid = id
    k = A[1]
    if k != 0:
        chil = A[2:2+k]
        T[id].left = chil[0]
        for i in range(k):
            if i != k-1:
                T[chil[i]].right = chil[i+1]
                T[chil[i]].parent = id
            else:
                T[chil[i]].parent = id            
D = [0]*n
def setDepth(u,p):#uはノードの番号、pはノードpの深さ。
    D[u] = p      #uより右下にあるノードの深さをDに保存し、かえす
    if T[u].right != NIL:
        setDepth(T[u].right,p)
    if T[u].left != NIL:
        setDepth(T[u].left,p+1)
    return D
def getDepth(u):
    d = 0
    while T[u].parent != NIL:
        u = T[u].parent
        d += 1
    return d
def findroot(u): #根をみつける
    while T[u].parent != NIL:
        u = T[u].parent
    return u
def printChildren(u):#番号uのノードの子供をlistでかえす
    child = []
    if T[u].left != NIL:
        c = T[u].left
        while c != NIL:
            child.append(c)
            c = T[c].right
    return child
def ppp():
	for i in range(n):
  		ccc = T[i]
  		print(i,ccc.parent,ccc.left,ccc.right)
#ここからもんだいによってかわる
r = findroot(firstid)
D = setDepth(r,0)
for i in range(n):
    nod = T[i]
    d = getDepth(i)
    s = "internal node"
    if nod.parent == NIL:
        s = "root"
    elif nod.left == NIL:
        s = "leaf"
    child = printChildren(i)
    print(f'node {i}: parent = {nod.parent}, depth = {d}, {s}, {child}')
