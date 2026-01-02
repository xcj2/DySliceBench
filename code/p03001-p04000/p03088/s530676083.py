import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

from itertools import product

def main():
    N = II()
    A, G, C, T = range(4)
    def code(c0, c1, c2):
        return c0 + 4 * c1 + 16 * c2
    dp = [0] * 64
    dp[code(T, T, T)] = 1
    for _ in range(N):
        pre = dp
        dp = [0] * 64
        for p1, p2, p3 in product(range(4), repeat=3):
            for cur in range(4):
                if (p2, p1, cur) in [(A, G, C), (A, C, G), (G, A, C)]:
                    continue
                if (p3, p1, cur) == (A, G, C):
                    continue
                if (p3, p2, cur) == (A, G, C):
                    continue
                dp[code(cur, p1, p2)] += pre[code(p1, p2, p3)]
                dp[code(cur, p1, p2)] %= MOD
    ans = sum(dp)

    return ans % MOD

print(main())