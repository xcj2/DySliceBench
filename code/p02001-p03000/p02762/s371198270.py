import math
import sys
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def init(n):
  for i in range(1,N+1):
    par[i] = i
    rnk[i] = 0
    size[i] = 1
def find(x):
  if par[x] == x:
    return x
  else:
    par[x] = find(par[x])
    return par[x]
def numfind(x):
  if par[x] == x:
    return size[x]
  else:
    return numfind(par[x])
def unite(x, y):
  x = find(x)
  y = find(y)
  if x == y:
    return
  if (rnk[x] < rnk[y]):
    par[x] = y
    size[y] += size[x]
  else:
    par[y] = x
    size[x] += size[y]
    if(rnk[x] == rnk[y]):
      rnk[x] += 1
def same(x, y):
  return find(x) == find(y)

N,M,K = IL()
ab = [IL() for i in range(M)]
cd = [IL() for i in range(K)]

par = [0 for i in range(N+1)]
rnk = [0 for i in range(N+1)]
size = [0 for i in range(N+1)]
init(N)

fr = [[] for i in range(N+1)]
bl = [[] for i in range(N+1)]
for a,b in ab:
  fr[a].append(b)
  fr[b].append(a)

for a,b in ab:
  if same(a,b):
    continue
  else:
    unite(a,b)

ans = [-1]*N
for i in range(1,N+1):
  cnt = numfind(i) - len(fr[i]) -1
  ans[i-1] = cnt

for c,d in cd:
  if same(c,d):
    ans[c-1] -= 1
    ans[d-1] -= 1
print(*ans)
