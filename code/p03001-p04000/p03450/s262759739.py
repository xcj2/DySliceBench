def solve(n, query):
    for l, r, d in query:
        if is_same(l, r):
            if d != diff(l, r):
                return 'No'
        else:
            unite(l, r, d)
    return 'Yes'


def find(x):
    if par[x] < 0:
        return x
    else:
        px = find(par[x])
        diff_weight[x] += diff_weight[par[x]]
        par[x] = px
        return px


def weight(x):
    find(x)
    return diff_weight[x]


def unite(x, y, w):
    w += diff_weight[x]-diff_weight[y]
    x = find(x)
    y = find(y)
    if x == y:
        return False
    else:
        if par[x] > par[y]:
            x, y = y, x
            w = -w
        par[x] += par[y]
        par[y] = x
        diff_weight[y] = w
        return True


def is_same(x, y):
    return find(x) == find(y)


def diff(x, y):
    return weight(y)-weight(x)


if __name__ == '__main__':
    n, m = map(int, input().split())
    par = [-1]*(n+1)
    diff_weight = [0]*(n+1)
    query = []
    for _ in range(m):
        l, r, d = map(int, input().split())
        query.append((l, r, d))
    print(solve(n, query))
