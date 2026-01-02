import sys
input = sys.stdin.readline
 
n,m,k = map(int,input().split())
ab = [set() for _ in range(n)]
cd = [[] * n for _ in range(n)]

 
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

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    unite(a - 1, b - 1)
    ab[a - 1].add(b - 1)
    ab[b - 1].add(a - 1)

for i in range(k):
    c, d = [int(x) for x in input().split()]
    if same(c - 1, d - 1):
        cd[c - 1].append(d - 1)
        cd[d - 1].append(c - 1)

ans = [0] * n

for i in range(n):
    ans[i] = size(i) - 1 - len(cd[i]) - len(ab[i])

print(*ans)


