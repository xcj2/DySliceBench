import sys
input = sys.stdin.readline
n,m = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
p = tuple(p)
chk = [[set(),set()] for i in range(n)]
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
      
def same(x,y):
    return find(x) == find(y)
  
par = [-1]*n
ans = 0
for i in range(m):
  x,y = [int(i) for i in input().split()]
  unite(x-1,y-1)

for i,pi in enumerate(p):
  if same(i,pi-1):
    ans += 1
    
print(ans)