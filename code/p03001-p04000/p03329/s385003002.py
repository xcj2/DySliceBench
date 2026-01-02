from collections import Counter
from functools import reduce
import fractions
import math
import statistics
import sys
import time
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]  # LIST INT
def LF(): return [float(x) for x in sys.stdin.readline().split()]  # LIST FLOAT
def LS(): return sys.stdin.readline().split()  # LIST STRING
def MI(): return map(int, sys.stdin.readline().split())  # MAP INT
def II(): return int(sys.stdin.readline())  # INPUT INT
def IS(): return input()  # INPUT STRING
def P(x): return print(x)
def C(x): return Counter(x)
def GCD_LIST(numbers):  # greatest common divisor
    return reduce(fractions.gcd, numbers)
def LCM_LIST(numbers):  # least common multiple
    return reduce(LCM, numbers)
def LCM(m, n):
    return (m * n // fractions.gcd(m, n))


# n = II()
# one = [1]
# six = [6 ** i for i in range(1, 6+1)]
# nine = [9 ** i for i in range(1, 5+1)]
# numbers = one + six + nine
# numbers.sort(reverse=True)

N = int(input())
dp = [INF] * 100001
dp[0], dp[1] = 0, 1
L = [1, 6, 36, 216, 1296, 7776, 46656, 9, 81, 729, 6561, 59049]
# dp[n]は，n円を引き出す最小引き出し回数
for i in range(2, 100001):
    for j in range(len(L)):
        if i-L[j] >= 0:
            dp[i] = min(dp[i-L[j]]+1, dp[i])
# 100円を引き出す時，まず，100-L[0] = 100-1=99で1円でのみで引き出すことを考える
# dp[100]にまずmin(dp[99]+1，INF)で99円引き出すための最小引き出し回数に1をたす（1円引き出す
# を考える
# 次に，その値と，94円から引き出すための最小回数+1とさっきのdp[99]を比較して，最小値を更新する
# 100000 * 10くらい 1000000くらい
print(dp[N])
