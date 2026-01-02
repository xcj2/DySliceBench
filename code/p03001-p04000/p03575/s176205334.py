n, m = map(int, input().split())
chk = []
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    chk.append((u,v))
chk = tuple(chk)

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

ans = 0
for i in range(m):
  par = [-1]*n
  for j in range(m):
    if i == j:
      continue
    else:
      unite(chk[j][0],chk[j][1])
  if size(0) != n:
    ans += 1
    
print(ans) 