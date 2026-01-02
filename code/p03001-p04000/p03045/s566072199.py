import sys
input = sys.stdin.readline
 
n,m = map(int,input().split())
 
#Union Find
par = [] #親
rank = [] #木の深さ
 
#初期化
for i in range(n):
    #par[i]:i rank[i]:0
    par.append(i)
    rank.append(0)
 
#木の根を求める
def find(x,par):
    if par[x] == x:
        return x
    else:
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
 
tank = []
for i in range(n):
    p = find(i,par)
    tank.append(p)
print(len(set(tank)))