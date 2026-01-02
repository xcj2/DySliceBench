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
import numpy as np

def main():
    N = II()
    A, G, C, T = 0, 1, 2, 3
    dp = np.zeros((N + 1, 4, 4, 4), int)
    dp[0, T, T, T] = 1
    for n in range(N):
        for p1, p2, p3 in product(range(4), repeat=3):
            for cur in range(4):
                if (p2, p1, cur) == (A, G, C):
                    continue
                if (p2, p1, cur) == (A, C, G):
                    continue
                if (p2, p1, cur) == (G, A, C):
                    continue
                if (p3, p1, cur) == (A, G, C):
                    continue
                if (p3, p2, cur) == (A, G, C):
                    continue
                dp[n + 1, cur, p1, p2] = \
                    (dp[n + 1, cur, p1, p2] + dp[n, p1, p2, p3]) % MOD
    ans = np.sum(dp[N])

    return ans % MOD

print(main())