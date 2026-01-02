import sys
input = sys.stdin.readline

def Find(x, par):
  if par[x] < 0:
    return x
  else:
    # 経路圧縮
    par[x] = Find(par[x], par)
    return par[x]

def Unite(x, y, par, rank):
  x = Find(x, par)
  y = Find(y, par)
  
  if x != y:
    z = par[x]*par[y]
    # rankの低い方を高い方につなげる
    if rank[x] < rank[y]:
      par[y] += par[x]
      par[x] = y
    else:
      par[x] += par[y]
      par[y] = x
      if rank[x] == rank[y]:
        rank[x] += 1
    return z
  else:
    return 0
    
def Same(x, y, par):
  return Find(x, par) == Find(y, par)
 
def Size(x, par):
  return -par[Find(x)]

n, m = map(int, input().split())
l = [[0, 0] for _ in range(m)]
for i in range(m):
  a, b = map(int, input().split())
  a, b = a-1, b-1
  l[i][0] = a
  l[i][1] = b

par = [-1]*n
rank = [0]*n

ans = [0]*m
ans[0] = n*(n-1)//2
for j in range(m-1):
  ans[j+1] = ans[j]-Unite(l[m-1-j][0], l[m-1-j][1], par, rank)

for i in reversed(range(m)):
  print(ans[i])
  