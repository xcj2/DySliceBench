import sys
from operator import itemgetter
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

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

N = I()
xlist = []
ylist = []

par=[0 for i in range(N)]
rnk=[0 for i in range(N)]
init(N)

for i in range(N):
  x, y = IL()
  xlist.append([x, i])
  ylist.append([y, i])
xlist.sort(key=itemgetter(0))
ylist.sort(key=itemgetter(0))

node = []
for i in range(N-1):
  x, xID = xlist[i]
  nextx, nextxID = xlist[i + 1]
  y, yID = ylist[i]
  nexty, nextyID = ylist[i + 1]
  
  node.append([nextx - x, xID, nextxID])
  node.append([nexty - y, yID, nextyID])
node.sort(key=itemgetter(0), reverse=True)

ans = 0
while node:
  val, i, j = node.pop()
  if same(i, j):
    continue
  else:
    unite(i, j)
    ans += val
print(ans)