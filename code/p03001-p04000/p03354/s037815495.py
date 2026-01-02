n,m = map(int,input().split())
p = list(map(int,input().split()))
info = [list(map(int,input().split())) for _ in range(m)]

par =[i for i in range(n+1)] 
rank=[0]*(n+1)

# xの根を見つける
def root(x):
  if par[x] == x:
    return x
  else:
    par[x] = root(par[x])
    return par[x]
  
# x,yの根が同じかどうかを返す（根が同じ:True、根が異なる:False）
def find(x, y):
  return root(x) == root(y)

# xとyの根を結合させる
def union(x, y):
  x = root(x)
  y = root(y)
  if rank[x] < rank[y]:
    par[x] = y
  else:
    par[y] = x
    if rank[x] == rank[y]:
      rank[x] += 1

for i in range(m):
  union(info[i][0],info[i][1])

a=[0]*(n+1)
for i in range(n):
  a[p[i]]=i+1

ans = 0 
for i in range(1,n+1):
  if find(i,a[i]):
    ans += 1
    
print(ans)