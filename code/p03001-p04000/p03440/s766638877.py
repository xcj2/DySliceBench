import heapq
N,M=map(int,input().split())
if M==N-1:
    print(0)
    exit()
if N<2*(N-M-1):
    print("Impossible")
    exit()
a=[int(i) for i in input().split()]
x=[0 for i in range(M)]
y=[0 for i in range(M)]
for i in range(M):
    x[i],y[i]=map(int,input().split())
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
for i in range(M):
    unite(x[i],y[i])
A=[find(i) for i in range(N)]
K=0
D=dict()
for i in range(N):
    if A[i] in D:
        D[A[i]].append((a[i],i))
    else:
        D[A[i]]=[(a[i],i)]
        K+=1
ans=0
used=[0 for i in range(N)]
for i in D:
    seq=min(D[i])
    ans+=seq[0]
    used[seq[1]]=1
q=[]
for i in range(N):
    if used[i]==0:
        heapq.heappush(q,(a[i],i))
for _ in range(2*(N-M-1)-K):
    s,t=heapq.heappop(q)
    ans+=s
print(ans)
