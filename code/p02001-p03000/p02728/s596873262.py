# 解説動画の通り
import sys

# grobalにmdを設定すること
class mint:
    def __init__(self, x):
        self.__x = x % md

    def __str__(self):
        return str(self.__x)

    def __neg__(self):
        return mint(-self.__x)

    def __add__(self, other):
        if isinstance(other, mint): other = other.__x
        return mint(self.__x + other)

    def __sub__(self, other):
        if isinstance(other, mint): other = other.__x
        return mint(self.__x - other)

    def __rsub__(self, other):
        return mint(other - self.__x)

    def __mul__(self, other):
        if isinstance(other, mint): other = other.__x
        return mint(self.__x * other)

    __radd__ = __add__
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, mint): other = other.__x
        return mint(self.__x * pow(other, md - 2, md))

    def __rtruediv__(self, other):
        return mint(other * pow(self.__x, md - 2, md))

    def __pow__(self, power, modulo=None):
        return mint(pow(self.__x, power, md))

md = 10 ** 9 + 7

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def nCr(com_n, com_r):
    if com_n < com_r: return 0
    return fac[com_n] * ifac[com_r] * ifac[com_n - com_r]

n_max = 200005
fac = [mint(1)]
for i in range(1, n_max + 1): fac.append(fac[-1] * i)
ifac = [mint(1)] * (n_max + 1)
ifac[n_max] /= fac[n_max]
for i in range(n_max - 1, 1, -1): ifac[i] = ifac[i + 1] * (i + 1)

class SubTree:
    # vが場合の数、sが頂点数（根を除く）
    def __init__(self, v, s):
        self.v = v
        self.s = s

    def __add__(self, other):
        t = other.s + 1
        v = self.v * other.v * nCr(self.s + t, t)
        s = self.s + t
        return SubTree(v, s)

    def __sub__(self, other):
        t = other.s + 1
        s = self.s - t
        v = self.v / (other.v * nCr(self.s, t))
        return SubTree(v, s)

def main():
    def dfs1(u=0, pu=-1):
        for v in to[u]:
            if v == pu: continue
            dfs1(v, u)
            dp[u] += dp[v]

    def dfs2(u=0, pu=-1):
        dpu = dp[u]
        for v in to[u]:
            if v == pu: continue
            dp[v] += dpu - dp[v]
            dfs2(v, u)

    n = II()
    to = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = MI1()
        to[a].append(b)
        to[b].append(a)
    dp = [SubTree(mint(1),0) for _ in range(n)]
    dfs1()
    dfs2()
    for a in dp: print(a.v)

main()
