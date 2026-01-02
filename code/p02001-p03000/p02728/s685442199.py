import sys
sys.setrecursionlimit(10**6)
MOD = 10**9 + 7

m = 2*10**5+5
fac = [0] * m
finv = [0] * m
inv = [0] * m


def COMBinitialize(m):
    fac[0] = 1
    finv[0] = 1
    if m > 1:
        fac[1] = 1
        finv[1] = 1
        inv[1] = 1
        for i in range(2, m):
            fac[i] = fac[i-1] * i % MOD
            inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
            finv[i] = finv[i - 1] * inv[i] % MOD


COMBinitialize(m)


def COMB(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


class modint():
    def __init__(self, value):
        self.value = value % MOD

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        return (modint(self.value + other.value) if isinstance(other, modint)
                else modint(self.value + other))

    def __sub__(self, other):
        return (modint(self.value - other.value) if isinstance(other, modint)
                else modint(self.value - other))

    def __mul__(self, other):
        return (modint(self.value * other.value) if isinstance(other, modint)
                else modint(self.value * other))

    def __truediv__(self, other):
        return (modint(self.value * pow(other.value, MOD - 2, MOD))
                if isinstance(other, modint)
                else modint(self.value * pow(other, MOD - 2, MOD)))

    def __pow__(self, other):
        return (modint(pow(self.value, other.value, MOD))
                if isinstance(other, modint)
                else modint(pow(self.value, other, MOD)))

    def __eq__(self, other):
        return (self.value == other.value if isinstance(other, modint)
                else self.value == (other % MOD))

    def __ne__(self, other):
        return (self.value == other.value if isinstance(other, modint)
                else self.value == (other % MOD))

    def __radd__(self, other):
        return (modint(other.value + self.value) if isinstance(other, modint)
                else modint(other + self.value))

    def __rsub__(self, other):
        return (modint(other.value - self.value) if isinstance(other, modint)
                else modint(other - self.value))

    def __rmul__(self, other):
        return (modint(other.value * self.value) if isinstance(other, modint)
                else modint(other * self.value))

    def __rtruediv__(self, other):
        return (modint(other.value * pow(self.value, MOD - 2, MOD))
                if isinstance(other, modint)
                else modint(other * pow(self.value, MOD - 2, MOD)))

    def __rpow__(self, other):
        return (modint(pow(other.value, self.value, MOD))
                if isinstance(other, modint)
                else modint(pow(other, self.value, MOD)))

    def modinv(self):
        return modint(pow(self.value, MOD - 2, MOD))


class DP():
    def __init__(self, dp=modint(1), t=0):
        self.dp = dp
        self.t = t

    def __iadd__(self, other):
        self.dp *= other.dp
        self.dp *= COMB(self.t+other.t, self.t)
        self.t += other.t
        return self

    def __sub__(self, other):
        res = DP(self.dp, self.t)
        res.t -= other.t
        res.dp /= COMB(res.t+other.t, res.t)
        res.dp /= other.dp
        return res

    def add_root(self):
        return DP(self.dp, self.t + 1)


def main():
    import sys
    input = sys.stdin.buffer.readline
    N = int(input())
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = (int(i) for i in input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)

    dp = [DP() for _ in range(N+5)]

    def dfs(v, p=-1):
        for u in edge[v]:
            if u == p:
                continue
            dfs(u, v)
            dp[v] += dp[u].add_root()

    def bfs(v, p=-1):
        for u in edge[v]:
            if u == p:
                continue
            d = dp[v] - dp[u].add_root()
            dp[u] += d.add_root()
            bfs(u, v)

    dfs(0)
    bfs(0)
    for i in range(N):
        print(dp[i].add_root().dp)


if __name__ == '__main__':
    main()
