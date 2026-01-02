import sys
sys.setrecursionlimit(10**7)

n, m = list(map(int, input().split()))
par = list(range(n+1))
dist = [0 for _ in range(n+1)]

def root(x):
  if x == par[x]:
    return x
  r = root(par[x])
  dist[x] += dist[par[x]]
  par[x] = r
  return r

def direct_cost(x):
  if x == par[x]:
    return 0
  return dist[x] + direct_cost(par[x])

def diff(x, y):
  return direct_cost(x) - direct_cost(y)

def unite(x, y, w):
  rootx = root(x)
  rooty = root(y)
  if rootx != rooty:
    if y != rooty:
      # 直接yにつなげる
      dist[rootx] = w - direct_cost(x)
    else:
      # 根につなげる
      dist[rootx] = w - (dist[x] - dist[y])
    # ここで親を更新
    par[rootx] = y
  else:
    return w == diff(x, y)

flag = True
for _ in range(m):
  l, r, d = list(map(int, input().split()))
  # 根が異なってたらとりあえず併合、同じならdifを取って整合性を確かめる
  a = unite(l, r, d)
  if a is not None:
    if a == False:
      flag = False
  """
  rootx, rooty = root(l), root(r)
  if rootx != rooty:
    if r != rooty:
      # 直接yにつなげる
      dist[rootx] = d - direct_cost(l)
    else:
      # yの根につなげる
      dist[rootx] = d - (dist[l] - dist[r])
    par[rootx] = l
  else:
    if d != diff(l, r):
      flag = False
  """
"""
[print("[{}]{}".format(idx, v), end=" ") for idx, v in enumerate(par)]
print()
[print("[{}]{}".format(idx, v), end=" ") for idx, v in enumerate(dist)]
print()
"""

print("Yes" if flag else "No")
  
