def Find(x, par):
  if par[x] < 0:
    return x
  else:
    par[x] = Find(par[x], par)
    return par[x]

def Unite(x, y, par, rank):
  x = Find(x, par)
  y = Find(y, par)
  
  if x != y:
    if rank[x] < rank[y]:
      par[x] = y
    else:
      par[y] = x
      if rank[x] == rank[y]:
        rank[x] += 1
    
def Same(x, y, par):
  return Find(x, par) == Find(y, par)
 
n, k, l = map(int, input().split())
rpar = [-1]*n
tpar = [-1]*n
rrank = [0]*n
trank = [0]*n
 
for i in range(k):
  p, q = map(int, input().split())
  p, q =p-1, q-1
  Unite(p,q, rpar, rrank) 

for i_ in range(l):
  p, q = map(int, input().split())
  p, q =p-1, q-1
  Unite(p,q, tpar, trank)

d = {}
IDs = [0]*n
for j in range(n):
  ID = Find(j, rpar)+(Find(j, tpar)+1)*10**8
  IDs[j] = ID
  if ID in d:
    d[ID] += 1
  else:
    d[ID] = 1


ans = ''
for j_ in range(n):
  if j_ != 0:
    ans += ' '
  ans += str(d[IDs[j_]])
print(ans)