N,M = map(int,input().split())
L = []
for i in range(M):
  L.append(list(map(int,input().split())))
def find(x,par):
  if par[x] == x:
    return x
  else:
    return find(par[x],par)
def unite(x,y,par,rank):
  x = find(x,par)
  y = find(y,par)
  if x != y:
    if rank[x] < rank[y]:
      par[x] = y
    else:
      par[y] = x
      if rank[x] == rank[y]:
        rank[x] += 1
def same(x,y,par):
  return find(x,par) == find(y,par)
cnt = 0
for i in range(M):
  par = []
  rank = [0]*N
  for j in range(N):
    par.append(j)
  TF = [True]*M
  TF[i] = False
  for k in range(M):
    if TF[k] == True:
      unite(L[k][0]-1,L[k][1]-1,par,rank)
  flag = True
  for l in range(N):
    for m in range(N):
      if not same(l,m,par):
        flag = False
  if flag:
    cnt += 1
print(M-cnt)