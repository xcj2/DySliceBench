import sys

def solve():
    N, Ma, Mb = map(int, input().split())
    table = [tuple(map(int, input().split())) for i in range(N)]

    g1 = half_rekkyo(N, Ma, Mb, table, 0, N // 2)
    g2 = half_rekkyo(N, Ma, Mb, table, N // 2, N - N // 2)

    inf = 100 * 40 + 1
    ans = inf

    if 0 in g1:
        ans = min(ans, g1[0])
    if 0 in g2:
        ans = min(ans, g2[0])

    for v1, c1 in g1.items():
        if -v1 in g2:
            tmp = c1 + g2[-v1]
            ans = min(ans, tmp)

    if ans < inf:
        print(ans)
    else:
        print(-1)

def half_rekkyo(N, Ma, Mb, table, s, m):
    res = dict()

    for comb in range(1, 2**m):
        v = 0
        cost = 0

        for i in range(m):
            if comb & (1 << i):
                a, b, c = table[s + i]
                v += b * Ma - a * Mb
                cost += c

        if v in res:
            res[v] = min(res[v], cost)
        else:
            res[v] = cost

    return res

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None


if __name__ == '__main__':
    solve()