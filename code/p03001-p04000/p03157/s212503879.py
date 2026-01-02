H,W=map(int,input().split())
S=[list(input()) for i in range(H)]
N=H*W
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
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for i in range(H):
    for j in range(W):
        for k in range(4):
            nx=dx[k]+i
            ny=dy[k]+j
            if 0<=nx<H and 0<=ny<W:
                if S[nx][ny]!=S[i][j]:
                    p=i*W+j
                    q=nx*W+ny
                    unite(p,q)
A=[find(i) for i in range(N)]
D=dict()
for j in range(N):
    i=A[j]
    if not(i in D):
        D[i]=[0,0]
    if S[j//W][j%W]=="#":
        D[i][1]+=1
    else:
        D[i][0]+=1
ans=0
for i in D:
    seq=D[i]
    ans+=seq[0]*seq[1]
print(ans)
