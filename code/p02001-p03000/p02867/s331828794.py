import sys
import math
MAX_INT = int(10e12)
MIN_INT = -MAX_INT
mod = 998244353
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def init(n):
  for i in range(N+1):
    par[i] = i
    rnk[i] = 0
def find(x):
  if par[x] == x:
    return x
  else:
    par[x] = find(par[x])
    return par[x]
def unite(x, y):
  x = find(x)
  y = find(y)
  if x == y:
    return
  if (rnk[x] < rnk[y]):
    par[x] = y
  else:
    par[y] = x
    if(rnk[x] == rnk[y]):
      rnk[x] += 1
def same(x, y):
  return find(x) == find(y)

N = I()
a = IL()
b = IL()

par = [0 for i in range(N+1)]
rnk = [0 for i in range(N+1)]
init(N)

adata = []
bdata = []
for i in range(N):
  adata.append([a[i], i])
  bdata.append([b[i], i])
adata.sort()
bdata.sort()
#print(adata)
#print(bdata)

a.sort()
b.sort()
f = 0
for i in range(N-1):
  atmp = a[i]
  btmp = b[i]
  atmp2 = a[i + 1]
  btmp2 = b[i + 1]
  if atmp > btmp:
    print("No")
    exit()
  if atmp2 > btmp2:
    print("No")
    exit()
  if atmp2 <= btmp:
    f = 1
else:
  if f == 1:
    print("Yes")
    exit()

for i in range(N-1):
  atmp, aID = adata[i]
  btmp, bID = bdata[i]
  #print("---")
  #print(atmp,aID)
  #print(btmp,bID)
  if aID == bID:
    break
  if same(aID, bID):
    break
  else:
    unite(aID, bID)
else:
  print("No")
  exit()
print("Yes")