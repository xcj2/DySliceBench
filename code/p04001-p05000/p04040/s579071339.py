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


def get_gates(h, w, a, b):
    i = 0
    gates = []
    while h-a-1-i >= 0 and b+i < w:
        gates.append((h-a-1-i, b+i))
        i += 1

    return gates


h, w, a, b = li()
MOD = 10**9 + 7

gates = get_gates(h,w,a,b)

inv = inv_mod(h+w, MOD)
fac = fact(h+w, MOD)
facInv = fact_inv(h+w, inv, MOD)

ans = 0
for ri, ci in gates:
    ans += nCr(ri+ci, ci , MOD, fac, facInv) * nCr(h+w-2-(ri+ci), w-1-ci, MOD, fac, facInv)
    ans %= MOD

print(ans)