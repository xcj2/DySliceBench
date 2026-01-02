#Union Find
import sys
input = sys.stdin.readline
 
n,m = map(int,input().split())

par = [i for i in range(n)] #親
rank = [0]*n #木の深さ

#木の根を求める
def find(x,par):
    if par[x] == x:
        return x
    else:
        par[x] = par[par[x]]
        return find(par[x],par)

#xとyの属する集合の併合
def unite(x,y,par,rank):
    x = find(x,par)
    y = find(y,par)
    
    if x != y:
        #xとyの属している集合が異なる時
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x]==rank[y]:
                rank[x] += 1

#xとyが同じ集合に属するかの判定
def same(x,y,par):
    return find(x,par) == find(y,par)

for i in range(m):
    X,Y,Z = map(int,input().split())
    unite(X-1,Y-1,par,rank)
 
tank = set([])
for i in range(n):
    p = find(i,par)
    tank.add(p)
print(len(tank))