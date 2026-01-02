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

n, m, k = map(int, input().split())

par = [-1]* n
rank = [0]*n

cnt1 = [0]*n
cnt2 = [0]*n
for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    Unite(a, b, par, rank)
    cnt1[a] += 1
    cnt1[b] += 1
for j in range(k):
    c, d = map(int, input().split())
    c, d = c-1, d-1
    if Same(c, d, par):
        cnt2[c] += 1
        cnt2[d] += 1

#print(par)
#print(cnt1)
#print(cnt2)
anss = [0]*n
for i in range(n):
    ans = Size(i, par) -1 - cnt1[i] - cnt2[i]
    #print(max(ans, 0))
    anss[i] = max(ans, 0)
print(*anss)
