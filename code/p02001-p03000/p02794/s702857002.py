import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n = ni()
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = na()
    g[a-1].append(b-1)
    g[b-1].append(a-1)

def dfs(cur, pre, g, par, od):
    par[cur] = pre
    od.append(cur)
    for e in g[cur]:
        if e == pre: continue
        dfs(e, cur, g, par, od)

par = [-1] * n
od = []
dfs(0, -1, g, par, od)

def lca(a, b, par):
    ps = set()
    q = a
    while q != -1:
        ps.add(q)
        q = par[q]
    while b != -1:
        if b in ps:
            return b
        b = par[b]
    raise

m = ni()
cons = [0] * n
for i in range(m):
    u, v = na()
    u -= 1
    v -= 1
    lc = lca(u, v, par)
    while u != lc:
        cons[u] |= 1<<i
        u = par[u]
    while v != lc:
        cons[v] |= 1<<i
        v = par[v]

def st(b, m):
    # b = copy(a)
    for i in range(m):
        for j in range(1<<m):
            if (j>>i&1) == 0:
                b[j|1<<i] += b[j]
    return b

def ist(b, m):
    # b = copy(a)
    for i in range(m):
        for j in range(1<<m):
            if (j>>i&1) == 0:
                b[j|1<<i] -= b[j]
    return b

dp = [1] * (1<<m)
for cur in range(1,n):
    for i in range(1<<m):
        if (i&cons[cur]) == cons[cur]:
            dp[i] *= 2

# dp = [None for _ in range(n)]
# for i in range(n-1,-1,-1):
#     cur = od[i]
#     my = [0] * (1<<m)
#     my[0] = 1
#     if cur != 0:
#         my[cons[cur]] += 1
#     my = st(my, m)
#
#     for e in g[cur]:
#         if e == par[cur]: continue
#         for j in range(1<<m):
#             my[j] = my[j] * dp[e][j]
#     dp[i] = my

    # dp[i] = ist(my, m)

dp = ist(dp, m)

print(dp[(1<<m)-1])
