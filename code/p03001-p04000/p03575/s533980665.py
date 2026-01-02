import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n,m = map(int,readline().split())
lst1 = [list(map(int,readline().split())) for i in range(m)]

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



ans = 0 #橋
for i in range(m):
    par = [-1]*n
    for j in range(m):
        if i == j:
            continue
        else:
            unite(lst1[j][0]-1,lst1[j][1]-1)
    if group_count() != 1:
        ans += 1
print(ans)
    


