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
    dp['TTT'] += 1
    for _ in range(N):
        pre = dp
        dp = Counter()
        for p1, p2, p3, cur in product('ACGT', repeat=4):
            if p2 + p1 + cur in ['AGC', 'GAC', 'ACG']:
                continue
            if p3 + p1 + cur == 'AGC':
                continue
            if p3 + p2 + cur == 'AGC':
                continue
            new = p2 + p1 + cur
            old = p3 + p2 + p1
            dp[new] = (dp[new] + pre[old]) % MOD
    ans = sum(dp.values())

    return ans % MOD

print(main())