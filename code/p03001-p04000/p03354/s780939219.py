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
P = list(map(int, input().split()))
P = [p-1 for p in P]

par = [-1]* n
rank = [0]*n

for i in range(m):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    Unite(x, y, par, rank)

ans = 0
for i in range(n):
    if P[i] == i:
        ans += 1
    else:
        if Same(i, P[i], par):
            ans += 1
print(ans)