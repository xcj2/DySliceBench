from collections import Counter
from functools import reduce
import fractions
import math
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


n, k = MI()
dp = [INF] * n
h = LI()
dp[0] = 0
for i in range(0, n-1):
    for j in range(1, k+1):
        if n <= i+j:
            continue
        dp[i+j] = min(dp[i] + abs(h[i]-h[i+j]), dp[i+j])
P(dp[n-1])
