def find(x):
    '''
    xの根を求める
    O(α(N))
    '''
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def union(x, y):
    '''
    xとyの属する集合を併合する
    '''
    x = find(x)
    y = find(y)
    
    if x == y:
        return False

    if par[x] > par[y]:
        x, y = y, x

    par[x] += par[y]
    par[y] = x
    return True


def size(x):
    '''
    xが属する集合の個数を求める
    '''
    return -par[find(x)]


def same(x, y):
    '''
    xとyが同じ集合に属するかを判定する
    '''
    return find(x) == find(y)


n, m = map(int, input().split())

par = [-1] * n
for _ in range(m):
    a, b = map(int, input().split())
    if not same(a-1, b-1):
        union(a-1, b-1)

res = 0
for i in range(n):
    res = max(res, size(i))

print(res)