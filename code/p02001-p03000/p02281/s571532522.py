
n=int(input())
T=[[]]*n
P=[-1]*(n+1)#n=1の対策、場当たり的だが
for i in range(n):
    id, left, right = map(int,input().split( ))
    T[id] =[left,right]
    P[right] = id
    P[left] = id

root=0

while P[root] !=-1:
    root = P[root]

#再帰的に行う

def preorder(u):
    global T
    L = []
#    if u != -1:
#        L.append(u)
#        L += (preorder(T[u][0]))
#        L += (preorder(T[u][1]))
#他も同様の変更
    L.append(u)
    if T[u][0] != -1:
        L += (preorder(T[u][0]))
    if T[u][1] != -1:
        L += (preorder(T[u][1]))
    return L

def inorder(u):
    global T
    L = []
    if T[u][0] != -1:
        L += (inorder(T[u][0]))
    L.append(u)
    if T[u][1] != -1:
        L += (inorder(T[u][1]))
    return L


def postorder(u):
    global T
    L = []
    if T[u][0] != -1:
        L += (postorder(T[u][0]))
    if T[u][1] != -1:
        L += (postorder(T[u][1]))
    L.append(u)
    return L
Pre= preorder(root)
In = inorder(root)
Post=postorder(root)
print("Preorder",end="\n ")
print(*Pre)
print("Inorder",end="\n ")
print(*In)
print("Postorder",end="\n ")
print(*Post)

