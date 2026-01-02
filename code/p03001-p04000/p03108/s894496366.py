import sys
input = sys.stdin.readline
from collections import deque
n,m = [int(i) for i in input().split()]
ab = deque([])
for i in range(m):
  a,b = [int(i) for i in input().split()]
  ab_appendleft = ab.appendleft
  ab_appendleft((a-1,b-1))
  
#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]
  
par = [-1]*n
ans = n*(n-1)//2
chk = deque([])
chk_appendleft = chk.appendleft
chk_appendleft(n*(n-1)//2)

for i in ab:
  if not same(i[0],i[1]):
    c = size(i[0])
    d = size(i[1])
    unite(i[0],i[1])
    ans -= c*d
    chk_appendleft(ans)
  else:
    chk_appendleft(ans)

chk = list(chk)[1:]
for i in chk:
  print(i)