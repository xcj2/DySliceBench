# xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


# xとyの属する集合の併合
def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return

    # sizeの大きいほうがx
    if par[x] > par[y]:
        x, y = y, x

    par[x] += par[y]
    par[y] = x


# xが属する集合の個数
def size(x):
    return -par[find(x)]


# xとyが同じ集合に属するかの判定
def same(x, y):
    return find(x) == find(y)


n, m = map(int, input().split())
e = [list(map(int, input().split())) for _ in range(m)]

res = 0
for i in range(m):
    par = [-1] * n
    flag = False

    for j in range(m):
        if i == j:
            continue
        a, b = e[j]
        union(a-1, b-1)
    
    for j in range(n):
        for k in range(j+1, n):
            if not same(j, k):
                flag = True
    
    if flag:
        res += 1

print(res)