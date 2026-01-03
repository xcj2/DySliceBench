N = int(input())

xy = [list(map(int,input().split()))+[i] for i in range(N)]

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

#xが属する集合の個数
def size(x):
    return -par[find(x)]


V = N#頂点の数、辺の数
v=[]

xy.sort()
for i in range(1,N):#[0][1]つなぐところ[2]距離
    v.append([xy[i-1][2],xy[i][2],min(abs(xy[i][0]-xy[i-1][0]),abs(xy[i][1]-xy[i-1][1]))])
xy.sort(key = lambda x:x[1])
for i in range(1,N):#[0][1]つなぐところ[2]距離
    v.append([xy[i-1][2],xy[i][2],min(abs(xy[i][0]-xy[i-1][0]),abs(xy[i][1]-xy[i-1][1]))])

v.sort(key = lambda x:x[2])

#初期化
#根なら-size,子なら親の頂点
par = [-1]*V

cost = 0

for i in range(0,len(v),1):
    if not same(v[i][0],v[i][1]):
        unite(v[i][0],v[i][1])
        cost+=v[i][2]

print(cost)