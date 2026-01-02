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
    # rankの低い方を高い方につなげる
    if rank[x] < rank[y]:
      par[y] += par[x]
      par[x] = y
    else:
      par[x] += par[y]
      par[y] = x
      if rank[x] == rank[y]:
        rank[x] += 1

def Same(x, y, par):
  return Find(x, par) == Find(y, par)

def Size(x, par):
  return -par[Find(x, par)]

n, m = map(int, input().split())
L = [[0, 0] for _ in range(m)]
for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    L[i][0] = a
    L[i][1] = b

par = [-1]* n
rank = [0]*n

ans = n*(n-1)//2
anss = [0]*m
for i in reversed(range(m)):
    anss[i] = ans
    a = L[i][0]
    b = L[i][1]
    if not Same(a, b, par):
        ans = max(0, ans-Size(a, par)*Size(b, par))
        Unite(a, b, par, rank)
    #print(par)

for i in range(m):
    print(anss[i])
