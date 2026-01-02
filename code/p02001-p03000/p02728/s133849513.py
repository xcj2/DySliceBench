import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n = ni()
g = []
for i in range(n): g.append([])
for i in range(n-1):
    x, y = na()
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)

dp = [0] * n
ep = [0] * n
des = [0] * n

def enumfif(n, mod):
    f = [0] * (n+1)
    invf = [0] * (n+1)
    f[0] = 1
    for i in range(1, n+1):
        f[i] = f[i-1] * i % mod

    a = f[n]
    b = mod
    p, q = 1, 0
    while b > 0:
        c = a//b
        d = a; a = b; b = d % b
        d = p; p = q; q = d-c*q
    invf[n] = p + mod if p < 0 else p
    for i in range(n-1,-1,-1):
        invf[i] = invf[i+1] * (i+1) % mod
    return f, invf

def C(n, r, mod, fif):
    if n < 0 or r < 0 or r > n:
        return 0
    return fif[0][n] * fif[1][r] * fif[1][n-r] % mod

mod = 1000000007
fif = enumfif(200005, mod)

sys.setrecursionlimit(200005)

def dfs(cur, pre, g):
    val = 1
    de = 0
    for e in g[cur]:
        if e == pre: continue
        dfs(e, cur, g)
        de += des[e]
        val = val * dp[e] * C(de, des[e], mod, fif) % mod
    dp[cur] = val
    des[cur] = de + 1

def dfs2(cur, pre, g):
    # print(cur, pre)
    for e in g[cur]:
        if e == pre: continue
        val = dp[cur] * fif[1][n-1] * fif[0][n-des[e]-1] * fif[0][des[e]] % mod
        dp[e] = val * C(n-1, n-des[e], mod, fif) % mod
        # val = dp[cur] * fif[1][n-1] * fif[0][n-des[e]-1] * fif[0][des[e]] * invl(dp[e], mod) % mod
        # dp[e] = dp[e] * val * C(n-1, n-des[e], mod, fif) % mod
        dfs2(e, cur, g)

def invl(a, mod):
    b = mod
    p = 1; q = 0
    while b > 0:
        c = a // b
        a, b = b, a%b
        p, q = q, p-c*q
    return p + mod if p < 0 else p


dfs(0, -1, g)
dfs2(0, -1, g)
for val in dp:
    print(val)
