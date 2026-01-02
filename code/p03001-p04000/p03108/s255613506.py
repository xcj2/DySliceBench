import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
ab = [[int(x) for x in input().split()] for _ in range(m)][::-1]

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

def cmb(n, k):
    return n * (n - 1) // 2
convinience = [0]

for i in ab:
    a, b = i
    res = convinience[-1]
    a -= 1
    b -= 1
    if find(a) == find(b):
        convinience.append(res)
        continue
    if size(a) > 1:
        res -= cmb(size(a), 2)
    if size(b) > 1:
        res -= cmb(size(b), 2)
    unite(a, b)
    res += cmb(size(a), 2)
    convinience.append(res)

convinience = convinience[1::][::-1] + [0]

ans = [0]
for i in range(m):
    ans.append(convinience[i] - convinience[i + 1] + ans[-1])
for i in ans[1:]:
    print(i)
