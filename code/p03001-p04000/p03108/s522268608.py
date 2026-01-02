import sys
sys.setrecursionlimit(10**7)

def find(x):#xの親を見つける
  if par[x] < 0:
    return x
  else:
    par[x] = find(par[x])
    return par[x]

def unite(x,y):#要素xとｙを併合させる
  x,y=find(x),find(y)#xとyの親の検索
  if x!=y:#親が異なる場合併合させる
    if x>y:
        x,y=y,x#小さい方をxとする. これにより要素の値が小さいものを優先して木の根とする. 
    par[x]+=par[y] #値を無向木の要素数の和にする.
    par[y]=x #枝側は根の位置を格納

def same(x, y):#要素xと要素yが同じ無向木に所属しているかを判定する
  return find(x) == find(y)#同じ値を持つか否か

def size(x):#要素xが所属する無向木の大きさを返す
  return-par[find(x)]

n, m = map(int, input().split()) #要素の数
par = [-1] * n #
path = []
for i in range(m):
  a, b = map(int, input().split())
  path.append([a-1, b-1])
ans_l = [n*(n-1)//2]
for i in range(m-1, 0, -1):
  if same(path[i][0], path[i][1]):
    ans_l.append(ans_l[-1])
    unite(path[i][0], path[i][1])
  else:
    ans_l.append(ans_l[-1] - size(path[i][0])*size(path[i][1]))
    unite(path[i][0], path[i][1])
for i in range(m-1, -1, -1):
  print(ans_l[i])