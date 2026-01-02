import sys
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
    num[i]=0
def find(x):
  if par[x]==x:
    return x
  else:
    return find(par[x])
def unite(x,y):
  if (y<x):
    par[x]=y
  else:
    par[y]=x
def same(x,y):
  return find(x)==find(y)
def cnt(x):
  if par[x]==x:
    res = num[x]
    return res
  else:
    if used[par[x]] == True:
      res = num[x] + ans[par[x]]
      return res
    else:
      return

N,Q = IL()
ab = [IL() for i in range(N-1)]
px = [IL() for i in range(Q)]

par=[0 for i in range(N+1)]
num=[0 for i in range(N+1)]

init(N)

for a,b in ab:
  unite(a,b)

for p,x in px:
  num[p] += x

ans = [0 for i in range(N+1)]
used = [False for i in range(N+1)]
for i in range(1,N+1):
  ans[i] = cnt(i)
  used[i] = True

print(" ".join(map(str,ans[1:])))