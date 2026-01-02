#Union Find

#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        tank = []
        while par[x] >= 0:
            tank.append(x)
            x = par[x]
        for elt in tank:
            par[elt] = x
        return x
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

import sys
input = sys.stdin.buffer.readline
 
n,m = map(int,input().split())

#初期化
#根なら-size,子なら親の頂点
par = [-1]*n

 
for _ in range(m):
    a,b = map(int,input().split())
    unite(a-1,b-1)
 
res = 0
for e in par:
    if e < 0:
        res = max(res,-e)
print(res)