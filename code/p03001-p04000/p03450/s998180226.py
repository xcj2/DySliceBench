n, m = list(map(int, input().split()))
par = list(range(n+1))
dis = [0] * (n+1)

def root(x):
  if x == par[x]:
    return x
  r = root(par[x])
  dis[x] += dis[par[x]]
  par[x] = r
  return r

def cost(x):
  # xからxの根までのコスト
  if x == par[x]:
    return 0
  return dis[x] + cost(par[x])

# 確かめ用
def unite(x, y, w):
  rootx = root(x)
  rooty = root(y)
  if rootx != rooty:
    if y != rooty:
      # 直接yにつなげる
      dis[rootx] = w - cost(x)
    else:
      # 根につなげる
      dis[rootx] = w - (dis[x] - dis[y])
    # ここで親を更新
    par[rootx] = y
  else:
    if w != cost(x) - cost(y):
      print("No")
      exit()


for _ in range(m):
  l, r, d = list(map(int, input().split()))
  # 根が違ってればマージ
  # 同じなら入力されたdistanceがこれまでの入力データからなる
  # 現在の木の構造から計算した数値とあっているか判断
  rootl, rootr = root(l), root(r)
  # 確かめ用
  a = unite(l, r, d)
  if a is not None:
    if a == False:
      flag = False

  """
  ちょっとなにがダメなのかわかんないので確かめる
  if rootl != rootr:
    # lをrにマージする
    if r == rootr:
      dis[rootl] = d - cost(l)
    else:
      dis[rootl] = d - (dis[l] - dis[r]) # (cost(l) - cost(r))
    par[rootl] = r
  else:
    # コストが同じかどうか
    if d == cost(l) - cost(r):
      continue
    else:
      print("No")
      exit()
  """
print("Yes")