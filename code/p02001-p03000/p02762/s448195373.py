N,M,K=map(int,input().split())  
par=[i for i in range(N)]
rank=[0]*(N)
friend=[0]*N
block=[0]*N
size=[1]*N
def find(x):
  if par[x]==x:
    return x
  else:
    par[x]=find(par[x])
    return par[x]

#同じ集合か判定
def same(x,y):
  return find(x)==find(y)

def union(x,y):
  x=find(x)
  y=find(y)
  if x==y:
    return 
  if rank[x]>rank[y]:
    par[y]=x
    size[x]+=size[y]
  else:
    par[x]=y
    size[y]+=size[x]
    if rank[x]==rank[y]:
      rank[y]+=1


for i in range(M):
  a,b=map(int,input().split())
  a-=1
  b-=1
  union(a,b)
  friend[a]+=1
  friend[b]+=1

for i in range(K):
  c,d=map(int,input().split())
  c-=1
  d-=1
  if same(c,d):
    block[c]+=1
    block[d]+=1
    
ans=[]
for i in range(N):
  ans.append(size[find(i)]-friend[i]-block[i]-1)
print(*ans)