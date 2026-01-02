#Union Find
import sys
input = sys.stdin.readline
 
n,m = map(int,input().split())

#根なら-size,子なら親の頂点
par = [-1]*n

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
    
    if x != y:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

def size(x):
    return -par[find(x)]

for i in range(m):
    X,Y,Z = map(int,input().split())
    unite(X-1,Y-1)
 
tank = set([])
for i in range(n):
    p = find(i)
    tank.add(p)
print(len(tank))