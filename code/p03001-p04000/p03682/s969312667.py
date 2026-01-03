def solve(query):
    q_x = sorted(query, key=lambda x: x[1])
    q_y = sorted(query, key=lambda x: x[2])

    g = set()

    for a, b in zip(q_x, q_x[1:]):
        s = a[0]
        t = b[0]
        w = min(abs(b[1]-a[1]), abs(b[2] - a[2]))
        g.add((w, s, t))

    for a, b in zip(q_y, q_y[1:]):
        s = a[0]
        t = b[0]
        w = min(abs(b[1]-a[1]), abs(b[2] - a[2]))
        g.add((w, s, t))

    _g = sorted(list(g))

    ans = 0
    for w, a, b in _g:
        if unite(a, b):
            ans += w
    return ans


def root(x):
    if x == par[x]:
        return x
    par[x] = y = root(par[x])
    return y


def unite(x, y):
    rt_x = root(x)
    rt_y = root(y)
    if rt_x == rt_y:
        return False
    if rt_x < rt_y:
        par[rt_y] = rt_x
    else:
        par[rt_x] = rt_y

    return True


if __name__ == '__main__':
    n = int(input())
    query = []
    par = [i for i in range(n+1)]
    for i in range(n):
        a, b = map(int, input().split())
        query.append((i, a, b))

    print(solve(query))
