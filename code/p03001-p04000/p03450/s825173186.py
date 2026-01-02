import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def Find(x, par, diff_weight):
  if par[x] < 0:
    return x
  else:
    # 経路圧縮
    px = Find(par[x], par, diff_weight)
    diff_weight[x] += diff_weight[par[x]]
    par[x] = px
    return px

def Unite(x, y, par, rank, diff_weight, w):
  w += diff_weight[x] - diff_weight[y]
  x = Find(x, par, diff_weight)
  y = Find(y, par, diff_weight)
  
  if x != y:
    # rankの低い方を高い方につなげる
    if rank[x] < rank[y]:
      x, y =  y, x
      w = -w
    if rank[x] == rank[y]:
        rank[x] += 1
    par[x] += par[y]
    par[y] = x
    diff_weight[y] = w

def Same(x, y, par, diff_weight):
  return Find(x, par,diff_weight) == Find(y, par, diff_weight)
 
def Size(x, par):
  return -par[Find(x)]

def Weight(x, par, diff_weight):
  Find(x, par, diff_weight)
  return diff_weight[x]

def Diff(x, y, par, diff_weight):
  return Weight(y, par, diff_weight)  - Weight(x, par, diff_weight)

par = [-1]*n
rank = [0]*n
diff_weight = [0]*n
for i in range(m):
  l, r, d = map(int, input().split())
  l, r = l-1 ,r-1
  if Same(l, r, par, diff_weight) == False:
    Unite(l, r, par, rank, diff_weight, d)
  else:
    if d != Diff(l, r, par, diff_weight):
      print('No')
      exit()
print('Yes')
  