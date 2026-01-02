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

n, m, k = map(int, input().split())

F = [0]*n
B = [0]*n

par = [-1]* n
rank = [0]*n

for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    F[a] += 1
    F[b] += 1
    Unite(a, b, par, rank)

for i in range(k):
    c, d = map(int, input().split())
    c, d = c-1, d-1
    if Same(c, d, par):
        B[c] += 1
        B[d] += 1

ans = [0]*n
for i in range(n):
    ans[i] = Size(i, par)-F[i]-B[i]-1
print(*ans)
