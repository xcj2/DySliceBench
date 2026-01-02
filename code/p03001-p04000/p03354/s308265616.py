def solve(p, query):
    ans = 0
    for a, b in query:
        unite(a, b)

    for pi in p:
        if is_same(pi, p[pi]):
            ans += 1

    return ans


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def is_same(x, y):
    return find(x) == find(y)


def unite(x, y):
    rt_x = find(x)
    rt_y = find(y)
    if rt_x == rt_y:
        return
    if rnk[rt_x] < rnk[rt_y]:
        par[rt_x] = rt_y
    else:
        par[rt_y] = rt_x
        if rnk[rt_x] == rnk[rt_y]:
            rnk[rt_x] += 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    query = []
    par, rnk = [0]*n, [0]*n
    p = list(map(int, input().split()))
    p = list(map(lambda x: x-1, p))

    for _ in range(m):
        a, b = map(int, input().split())
        query.append((a-1, b-1))

    for i in range(n):
        par[i] = i

    print(solve(p, query))
