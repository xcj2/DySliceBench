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

#xが属する集合の個数
def size(x):
    return -par[find(x)]

n,m = map(int,input().split())

#根なら-size,子なら親の頂点
par = [-1]*n
lan = [[] for _ in [0]*m]
for pt in range(n):
    l = tuple(map(int,input().split()))
    for i in range(1,len(l)):
        lan[l[i]-1].append(pt)

for i in range(m):
    for j in range(1,len(lan[i])):
        unite(lan[i][0],lan[i][j])

cnt = 0
for e in par:
    if e < 0:
        cnt += 1

if cnt == 1:
    print('YES')
else:
    print('NO')