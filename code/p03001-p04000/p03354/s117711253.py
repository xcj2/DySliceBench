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

def main():
  global N 
  N, M = map(int, input().split())
  global par 
  par = [-1] * N
  p = list(map(int, input().split()))
  for i in range(M):
    x, y = map(int, input().split())
    unite(x-1, y-1)
  ans = 0
  for i in range(N):
    if same(i, p[i]-1):
      ans += 1
  print(ans)

if __name__ == "__main__":
  main()
