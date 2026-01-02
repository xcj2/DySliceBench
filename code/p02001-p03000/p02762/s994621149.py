import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

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

#初期化
#根なら-size,子なら親の頂点
par = [-1]*n

num = [0]*n

for i in range(m):
    a,b = map(int,input().split())
    unite(a-1,b-1)
    num[a-1] += 1
    num[b-1] += 1

edge = [[] for i in range(n)]

for i in range(k):
    c,d = map(int,input().split())
    edge[c-1].append(d-1)
    edge[d-1].append(c-1)


for i in range(n):
    cnt = size(i) - num[i] - 1
    for e in edge[i]:
        if same(e,i):
            cnt -= 1
    print(cnt,end=' ')
