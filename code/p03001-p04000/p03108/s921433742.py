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


edge = [tuple(map(int,input().split())) for i in range(m)]
edge = edge[::-1]
for i in range(m):
    edge[i] = (edge[i][0]-1,edge[i][1]-1)

res = []
for i in range(m):
    fi = find(edge[i][0])
    se = find(edge[i][1])
    if fi == se:
        res.append(0)
    else:
        res.append(size(fi)*size(se))
        unite(fi,se)
ass = 0
for i in range(m):
    ass += res[m-1-i]
    print(ass)