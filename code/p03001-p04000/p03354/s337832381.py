n,m = [int(x) for x in input().strip().split()]
par = list(range(n))
rank = [0]*n

def find(x):
  if par[x]==x:
    return x
  else:
    par[x] = find(par[x])
    return par[x]

def unite(x,y):
  x,y = map(find, (x,y))
  if x==y:
    return
  if rank[x]<rank[y]:
    par[x] = y
  else:
    par[y] = x
    if rank[x]==rank[y]:
      rank[x]+=1

def same(x,y):
  return find(x)==find(y)

p = [int(x) for x in input().strip().split()]
for _ in range(m):
  x,y = [int(z)-1 for z in input().strip().split()]
  unite(x,y)

p = sorted([(z,i) for i,z in enumerate(p)], reverse=True)
print(sum([same(val-1,idx) for val,idx in p]))