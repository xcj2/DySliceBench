import sys
MAX_INT = int(10e9)
MIN_NUM = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

# Union-Find #
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
        num[y]=num[x]+num[y]
    else:
        par[y]=x
        if(rnk[x]==rnk[y]):
            rnk[x]+=1
        num[x]=num[x]+num[y]
def same(x,y):
    return find(x)==find(y)

N,M = IL()
ab = [IL() for i in range(M)]
ans = N*(N-1)//2
data = []
par=[0 for i in range(N+1)]
rnk=[0 for i in range(N+1)]
num=[1 for i in range(N+1)]
init(N)

data.append(ans)
for i in range(M-1,-1,-1):
  a,b = ab[i]
  if same(a, b):
    data.append(ans)
  else:
    ans -= num[find(a)]*num[find(b)]
    unite(a, b)
    data.append(ans)

for i in range(M-1,-1,-1):
  print(data[i])