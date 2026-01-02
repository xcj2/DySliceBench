import sys
input = sys.stdin.readline
import bisect
n,m,k = [int(i) for i in input().split()]
ans = [-1]*n

def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

def size(x):
    return -par[find(x)]

par = [-1]*n
g = [[] * n for i in range(n)]
for i in range(m):
  a,b = [int(i) for i in input().split()]
  unite(a-1,b-1)
  ans[a-1] -= 1
  ans[b-1] -= 1
  
def same(x,y):
    return find(x) == find(y)
for i in range(k):
  u, v = map(int, input().split())
  if same(u-1,v-1):
    ans[u-1] -= 1
    ans[v-1] -= 1
  
for i in range(n):
  ans[i] += size(i)
  
print(*ans)