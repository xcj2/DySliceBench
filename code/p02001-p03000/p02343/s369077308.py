import sys
readline = sys.stdin.buffer.readline

n,q= map(int,readline().split())

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

"""
uniteでまとめ、findで見つける。
n(要素数)だけ最初に付け加えること。
"""

for i in range(q):
    com,a,b = map(int,readline().split())
    if com:
        if same(a,b):
            print(1)
        else:
            print(0)
    else:
        unite(a,b)
