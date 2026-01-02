


MAX = 10000
NIL = -1

class Node:
    def __init__(self):
        self.parent = NIL
        self.left = 0
        self.right = 0

# 先行順巡回
def preParse(u):
    if u == NIL: return
    print(" %d" % u ,end="")
    preParse(T[u].left)
    preParse(T[u].right)

# 中間順巡回
def inParse(u):
    if u == NIL: return
    inParse(T[u].left)
    print(" %d" % u ,end="")
    inParse(T[u].right)
# 後行順巡回
def postParse(u):
    if u == NIL: return
    postParse(T[u].left)
    postParse(T[u].right)
    print(" %d" % u ,end="")

n = int(input())

T = []
# n個のノードを用意
for i in range(n):
    node = Node()
    T.append(node)




for i in range(n):
    v,l,r = map(int,input().split())
    T[v].left = l
    T[v].right = r
    if l != NIL:
        T[l].parent = v
    if r != NIL:
        T[r].parent = v


for i in range(n):
    if T[i].parent == NIL:
        root = i

print("Preorder")
preParse(root)
print()
print("Inorder")
inParse(root)
print()
print("Postorder")
postParse(root)
print()

