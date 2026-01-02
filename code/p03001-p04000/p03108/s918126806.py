def find(x):
    if par[x] == x:
        return x
    else:
        return find(par[x])

def unite(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        if rank[x] < rank[y]:
            par[x] = y
            size[y] += size[x]
        else:
            par[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1

def same(x, y):
    return find(x) == find(y)

#初期化
n, m = map(int, input().split())
par = [0]*n
for i in range(n):
    par[i] = i #まず全ての値を根に置く
rank = [1]*n #深さ
size = [1]*n #根iにおけるグループサイズ

edge = [tuple(map(int, input().split())) for i in range(m)]
edge = edge[::-1]
for i in range(m):
    edge[i] = (edge[i][0]-1, edge[i][1]-1)

res = []
for i in range(m):
    fi = find(edge[i][0])
    se = find(edge[i][1])
    if fi == se:
        res.append(0)
    else:
        res.append(size[fi]*size[se])
        unite(fi, se)
ass = 0
for i in range(m):
    ass += res[m-1-i]
    print(ass)

