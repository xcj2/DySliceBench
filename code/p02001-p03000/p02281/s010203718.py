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
D = [0]*n
def setDepth(u,p):#uはノードの番号、pはノードpの深さ。
    if u == NIL:
        return
    D[u] = p      #uより下にあるノードの深さをDに保存し、かえす
    if T[u].left != NIL:
        setDepth(T[u].left,p+1)
    if T[u].right != NIL:
        setDepth(T[u].right,p+1)
    return D
H = [0]*n
def setHeight(u,H):
    hl = 0
    hr = 0
    if T[u].left != NIL:
        hl = 1 + setHeight(T[u].left,H)
    if T[u].right != NIL:
        hr = 1 + setHeight(T[u].right,H)
    ret = max(hl,hr)
    H[u] = ret
    return ret
def getDegree(u):
    cc = 0
    if T[i].left != NIL:
        cc += 1
    if T[i].right != NIL:
        cc += 1
    return cc
def getDepth(u):
    d = 0
    while T[u].parent != NIL:
        u = T[u].parent
        d += 1
    return d
def getBrother(u):
    if T[u].parent == NIL:
        return NIL
    elif T[T[u].parent].left == u:
        return T[T[u].parent].right
    elif T[T[u].parent].right == u:
        return T[T[u].parent].left
def printChildren(u):#番号uのノードの子供をlistでかえす
    child = []
    if T[u].left != NIL:
        child.append(T[u].left)
    if T[u].right != NIL:
        child.append(T[u].right)
    return child
def ppp():
	for i in range(n):
  		ccc = T[i]
  		print(i,ccc.parent,ccc.left,ccc.right)
def findroot(u): #根をみつける
    while T[u].parent != NIL:
        u = T[u].parent
    return u
#巡回
rl = []
def rootleft(u,rl): #どのパターンでもrootからスタート
    if u == NIL:
        return
    rl.append(u)
    rootleft(T[u].left,rl)
    rootleft(T[u].right,rl)
lro = []
def leftroot(u,lro):
    if u == NIL:
        return
    leftroot(T[u].left,lro)
    lro.append(u)
    leftroot(T[u].right,lro)
lri = []
def leftright(u,lri):
    if u == NIL:
        return
    leftright(T[u].left,lri)
    leftright(T[u].right,lri)
    lri.append(u)
#ここから入力
firstid = 0
for i in range(n):
    id,left,right = map(int,input().split())
    if n == 0:
        firstid = id
    if left != NIL:
        T[id].left = left
        T[left].parent = id
    if right != NIL:
        T[id].right = right
        T[right].parent = id
r = findroot(firstid)
D = setDepth(r,0)
setHeight(r,H)
leftright(r,lri)
leftroot(r,lro)
rootleft(r,rl)
s0 = " ".join(map(str,rl))
s1 = " ".join(map(str,lro))
s2 = " ".join(map(str,lri))
print("Preorder")
print(" "+s0)
print("Inorder")
print(" "+s1)
print("Postorder")
print(" "+s2)
