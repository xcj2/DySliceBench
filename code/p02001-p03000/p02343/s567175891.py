import sys

def solve():
    n, q = map(int, sys.stdin.readline().split())
    ds = [[i] for i in range(n)]
    n2s = [i for i in range(n)]
    ans = []

    for lp in range(q):
        c, x, y = map(int, sys.stdin.readline().split())

        if c == 0:
            merge(ds, n2s, x, y)
        else:
            ans.append(1 if n2s[x] == n2s[y] else 0)

    print(*ans, sep='\n')

def merge(ds, n2s, x, y):
    u = n2s[x]
    v = n2s[y]

    if u == v:
        return None

    if len(ds[u]) < len(ds[v]):
        ds[v].extend(ds[u])
        for w in ds[u]:
            n2s[w] = v
        del ds[u][:]
    else:
        ds[u].extend(ds[v])
        for w in ds[v]:
            n2s[w] = u
        del ds[v][:]

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

if __name__ == '__main__':
    solve()