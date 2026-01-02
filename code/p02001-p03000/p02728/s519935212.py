#!python3

import sys
sys.setrecursionlimit(10 ** 6)

MOD = 10 ** 9 + 7


class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, MOD - 2, MOD))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, MOD))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, MOD - 2, MOD))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, MOD))
        )


LI = lambda: list(map(int, input().split()))

# input
N = int(input())
AB = [LI() for _ in range(N - 1)]

# params
links = [[] for i in range(N)]
dp = [ModInt(1) for _ in range(N)]
c = [1] * N

MAX = 2 * (10 ** 5) + 5
fac, finv, inv = [None] * MAX, [None] * MAX, [None] * MAX


def comb_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = -inv[MOD%i] * int(MOD / i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD


def comb(n, k):
    if n < k or n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


def create_links():
    for a, b in AB:
        links[a - 1].append(b - 1)
        links[b - 1].append(a - 1)
    return links


def dfs1(v, p=-1):
    for u in links[v]:
        if u == p:
            continue
        dfs1(u, v)
        c[v] += c[u]
        dp[v] *= dp[u]
        dp[v] *= finv[c[u]]
    dp[v] *= fac[c[v] - 1]


def dfs2(v, p=-1):
    for u in links[v]:
        if u == p:
            continue
        dp[u] = dp[v] * c[u] * inv[(N - c[u])]
        dfs2(u, v)


def main():
    comb_init()
    create_links()
    dfs1(0)
    dfs2(0)
    [print(ans) for ans in dp]


if __name__ == "__main__":
    main()
