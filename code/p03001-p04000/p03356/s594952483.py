import sys
input = sys.stdin.readline
n,m = map(int,input().split())
p = [int(i) for i in input().split()]
par = [-1]*n
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
  
for i in range(m):
  x,y = [int(i) for i in input().split()]
  unite(x-1,y-1)
  
ans = 0
for i,pi in enumerate(p):
  if pi == i+1:
    ans += 1
  else:
    if same(pi-1,i):
      ans += 1
      
print(ans) 