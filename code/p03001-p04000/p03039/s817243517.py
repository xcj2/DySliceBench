import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


n, m, k = li()
MOD = 10**9 + 7

ans = 0


# nの逆元のリスト
def inv_mod(n: int, mod: int) -> list:
    inv = [0, 1]
    for i in range(2, n + 1):
        inv.append(mod - ((mod // i) * inv[mod % i]) % mod)
    return inv


# nの階乗のリスト
def fact(n: int, mod: int) -> list:
    fac = [1, 1]
    res = 1
    for i in range(2, n + 1):
        res = res * i % mod
        fac.append(res)
    return fac


# nの階乗の逆元のリスト
def fact_inv(n: int, inv: list, mod: int) -> list:
    facInv = [1, 1]
    for i in range(2, n + 1):
        facInv.append(facInv[i - 1] * inv[i] % mod)
    return facInv


# 二項係数
def nCr(n: int, r: int, mod: int, fac: list, facInv: list) -> int:
    if not (0 <= r and r <= n):
        return 0

    return ((fac[n] * facInv[r]) % mod) * facInv[n - r] % mod


def onedim(width: int, depth: int, mod: int):
    ret = 0
    for d in range(width):
        ret += depth**2 * (width - d) * d * nCr(m*n-2, k-2, mod, fac, facInv)
        ret %= mod

    return ret

fac = fact(n*m+1, MOD)
facInv = fact_inv(n*m, inv_mod(m*n+1, MOD), MOD)

print((onedim(n, m, MOD) + onedim(m, n, MOD)) % MOD)