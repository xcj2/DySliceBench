def find(x):
    '''
    xの根を求める
    '''
    if par[x] < 0:
        return x
    else:
        p = find(par[x])
        diff_w[x] += diff_w[par[x]]
        par[x] = p
        return p


def weight(x):
    '''
    xの根からの距離を求める
    '''
    find(x)
    return diff_w[x]


def union(x, y, w):
    '''
    w[y] = w[x] + w となるようにxとyの属する集合を併合する
    '''
    w += diff_w[x] - diff_w[y]
    x = find(x)
    y = find(y)
    
    if x == y:
        return False

    if par[x] > par[y]:
        x, y = y, x
        w = -w
    par[x] += par[y]
    par[y] = x
    diff_w[y] = w
    return True


def same(x, y):
    '''
    xとyが同じ集合に属するかを判定する
    '''
    return find(x) == find(y)


def size(x):
    '''
    xが属する集合の個数を求める
    '''
    return -par[find(x)]


def diff(x, y):
    '''
    xとyが同じ集合に属するときの w[y] - w[x] を求める
    '''
    return weight(y) - weight(x)


n, m = map(int, input().split())

par = [-1] * n
diff_w = [0] * n

for _ in range(m):
    l, r, d = map(int, input().split())

    if same(l-1, r-1):
        if diff(l-1, r-1) != d:
            print('No')
            exit()
    else:
        union(l-1, r-1, d)

print('Yes')