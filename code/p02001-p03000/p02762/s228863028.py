#Union Find

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

#根なら-size,子なら親の頂点
n,m,k = [int(i) for i in input().split()]
par = [-1]*n
ans = [-1]*n

import sys
input = sys.stdin.readline

for _ in range(m):
  a,b = [int(j) for j in input().split()]
  unite(a-1,b-1)
  ans[a-1] -= 1
  ans[b-1] -= 1

for _ in range(k):
  c,d = [int(i) for i in input().split()]
  if same(c-1,d-1):
    ans[c-1] -= 1
    ans[d-1] -= 1
    
for i in range(n):
  ans[i] += size(i)
  
ans = list(map(str,ans))
print(' '.join(ans))