N,M=map(int,input().split())
P=[0]+list(map(int,input().split()))

#Union-find
U=[i for i in range(N+1)] #根の頂点

#根を与える関数
def root(x):
    global U
    if x==U[x]:
        return x
    else:
        U[x]=root(U[x])  #経路圧縮
        return U[x]

#併合関数
def unite(x,y):
    global U
    if root(x)!=root(y):
        U[root(x)]=root(y)

#判定関数
def same(x,y):
    global U
    if root(x)==root(y):
        return 1
    else:
        return 0

for j in range(M):
    X,Y=map(int,input().split())
    unite(X,Y)

ans=0
for k in range(1,N+1):
    ans+=same(k,P[k])

print(ans)
    

