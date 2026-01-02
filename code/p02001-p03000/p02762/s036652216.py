def find(x):
    if par[x]<0:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
 
def unite(x,y):
  x,y=find(x),find(y)
  if x!=y:
    if x>y:
        x,y=y,x
    par[x]+=par[y]
    par[y]=x
    
def same(x,y):
  return find(x)==find(y)
 
def size(x):
  return-par[find(x)]
 
N,M,K = map(int,input().split())
par=[-1]*N
B = [set() for _ in range(N)]
FF = [0]*N
for _ in range(M):
    a,b = map(int,input().split())
    unite(a-1,b-1)
    FF[a-1] += 1
    FF[b-1] += 1
# print(F)
for j in range(K):
    a,b = map(int,input().split())
    B[a-1].add(b-1)
    B[b-1].add(a-1)

Y = []
for i in range(N):
    y = size(i) - FF[i] -1
    for b in B[i]:
        if same(i,b):
            y += -1
    Y.append(str(y))
print(" ".join(Y))
