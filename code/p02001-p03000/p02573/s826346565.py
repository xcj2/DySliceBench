import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,m = map(int,readline().split())

#最も大きなunionの大きさが答え
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

#xが属するグループの要素全てを返す
def members(x):
    root = find(x)
    return [i for i in range(n) if find(i) == root]

#全ての根の要素をlistで返す(一個下の関数で使う)
def roots():
    return [i for i,x in enumerate(par) if x < 0]

#グループ数を返す
def group_count():
    return len(roots())

#根をkey,そのグループに含まれる要素をvalueとして全てを辞書型で返す
def all_group_members():
    return {r: members(r) for r in roots()}

#初期化
#根なら-size,子なら親の頂点
par = [-1]*n

AB = []
for i in range(m):
    a,b = map(int,readline().split())
    a,b = a-1,b-1
    unite(a,b)

ans = 0
for i in par:
    if i < 0:
        ans = max(ans,-i)
print(ans)
