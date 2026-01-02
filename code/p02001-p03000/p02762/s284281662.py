import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

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

n, m, k = map(int, input().split())
par = [-1]*n
f = [set() for _ in range(n)]
b = [set() for _ in range(n)]
for _ in range(m):
    a, _b = map(int, input().split())
    f[a-1].add(_b-1)
    f[_b-1].add(a-1)
    unite(a-1, _b-1)
for _ in range(k):
    a, _b = map(int, input().split())
    b[a-1].add(_b-1)
    b[_b-1].add(a-1)

for i in range(n):
    ans = size(i)-len(f[i])-1
    for node in b[i]-f[i]:
        if same(i, node):
            ans -= 1
    print(ans, end=" " if i!=n-1 else "\n")
