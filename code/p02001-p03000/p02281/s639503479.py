def prePhase(u):
    left,right=T[u]
    if u==-1:return
    print(" {}".format(u), end="")
    prePhase(left)
    prePhase(right)


def inPhase(u):
    left,right=T[u]
    if u==-1:return
    inPhase(left)
    print(" {}".format(u), end="")
    inPhase(right)


def postPhase(u):
    left,right=T[u]
    if u==-1:return
    postPhase(left)
    postPhase(right)
    print(" {}".format(u), end="")


n=int(input())
A=sorted([list(map(int,input().split())) for i in range(n)])
T=[]
top=[i for i in range(n)]
for i in range(n):
    B=A[i]
    node,left,right=B[0],B[1],B[2]
    if left!=-1:top.remove(left)
    if right!=-1:top.remove(right)
    T.append([left,right])
top=top[0]

print("Preorder")
prePhase(top)
print()
print("Inorder")
inPhase(top)
print()
print("Postorder")
postPhase(top)
print()
