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

from collections import Counter
from itertools import product

def main():
    N = II()
    dp = Counter()
    dp['000'] += 1
    for _ in range(N):
        pre = dp
        dp = Counter()
        for (p3, p2, p1), n in pre.items():
            for cur in 'AGCT':
                new = p2 + p1 + cur
                if new in ['AGC', 'GAC', 'ACG']:
                    continue
                if p3 + p1 + cur == 'AGC':
                    continue
                if p3 + p2 + cur == 'AGC':
                    continue
                dp[new] = (dp[new] + n) % MOD
    ans = sum(dp.values())

    return ans % MOD

print(main())