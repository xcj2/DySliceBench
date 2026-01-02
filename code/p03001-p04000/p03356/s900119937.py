N,M=map(int, input().split()) 
P=list(map(int,input().split()))
par=[i for i in range(N+1)]
rank=[0]*(N+1)
#根
def find(x):
  if x==par[x]:
    return x
  else:
    par[x]=find(par[x])
    return par[x]
  
def find(x):
    if x == par[x]:
        return x
    par[x] = find(par[x])
    return par[x]
  
#同じ集合か判定
def same(x,y):
  return find(x)==find(y)

def union(x,y):
  x=find(x)
  y=find(y)
  if x==y:
    return 0
  if rank[x]<rank[y]:
    par[x]=y
  else:
    par[y]=x
    if rank[x]==rank[y]:
      rank[x]+=1

for i in range(M):
  a,b=map(int,input().split())
  union(a,b)

ans=0
for i in range(1,N+1):
  if same(P[i-1],i):
    ans+=1
print(ans)
 