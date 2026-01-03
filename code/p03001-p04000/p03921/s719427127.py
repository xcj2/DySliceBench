N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append([int(i)-1 for i in input().split()][1:])
K=[len(L[i]) for i in range(N)]
X=[-1 for i in range(M)]
for i in range(N):
    for j in range(K[i]):
        if X[L[i][j]]==-1:
            X[L[i][j]]=i
par=[0 for i in range(N)]
rnk=[0 for i in range(N)]
def init(n):
    for i in range(N):
        par[i]=i
        rnk[i]=0
def find(x):
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
def unite(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return
    if (rnk[x]<rnk[y]):
        par[x]=y
    else:
        par[y]=x
        if(rnk[x]==rnk[y]):
            rnk[x]+=1
def same(x,y):
    return find(x)==find(y)
init(N)
for i in range(N):
    for j in range(K[i]):
        unite(i,X[L[i][j]])
for i in range(1,N):
    if not(same(0,i)):
        print("NO")
        exit()
print("YES")
