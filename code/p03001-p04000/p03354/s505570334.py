def solve():
  n, m = map(int,input().split())
  plst = list(map(int,input().split()))
  pare_inds = [i for i in range(n)]
  rank = [0 for i in range(n)]
  
  def find(x):
    p = pare_inds[x]
    if p == x:
      return x
    a = find(p)
    pare_inds[x] = a
    return a
  
  def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
      return
    if rank[x] < rank[y]:
      pare_inds[x] = y
    else:
      pare_inds[y] = x
      if rank[x] == rank[y]:
        rank[x] += 1

  def same(x, y):
    return find(x) == find(y)

  for i in range(m):
    x, y = map(int,input().split())
    x, y = x - 1, y - 1
    unite(x, y)
  
  ans = 0
  for i in range(n):
    if same(i, plst[i] - 1):
      ans += 1

  print(ans)
solve()