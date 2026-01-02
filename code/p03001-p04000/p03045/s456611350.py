#Union Find

#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
      
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

n,m = [int(i) for i in input().split()]
par = [-1]*n
for i in range(m):
  x,y,z = [int(i)-1 for i in input().split()]
  unite(x,y)
  
chk = []
for i in range(n):
  chk_append = chk.append
  chk_append(find(i))
  
chk = set(chk)
print(len(chk))