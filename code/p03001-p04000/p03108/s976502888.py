N,M = map(int,input().split())
L = []
for i in range(M):
  L.append(list(map(int,input().split())))
L.reverse()
par = []
rank = [0]*N
size = [1]*N
for i in range(N):
  par.append(i)
def find(x,par):
  if x == par[x]:      
    return x
  else:
    return find(par[x],par)
def unite(x,y,par,rank,size):
  x = find(x,par)
  y = find(y,par)          
  if x != y:
    if rank[x] < rank[y]: 
      par[x] = y
      size[y] += size[x]
    else:
      par[y] = x
      size[x] += size[y]
      if rank[x] == rank[y]:
        rank[x] += 1
def same(x,y,par):
  return find(x,par) == find(y,par)

res = []
for i in range(M):
  A = find(L[i][0]-1,par)
  B = find(L[i][1]-1,par)
  if A == B:
    res.append(0)
  else:
    res.append(size[A]*size[B])
    unite(A,B,par,rank,size)
ans = 0
for i in range(M):
  ans += res[M-i-1]
  print(ans)