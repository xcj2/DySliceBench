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


n = II()
happiness = [LI() for _ in range(n)]
dp = [[0 for i in range(3)] for i in range(n+1)]
for i in range(n):
    dp[i+1][0] = max(dp[i][1]+happiness[i][0], dp[i][2]+happiness[i][0])
    dp[i+1][1] = max(dp[i][0]+happiness[i][1], dp[i][2]+happiness[i][1])
    dp[i+1][2] = max(dp[i][0]+happiness[i][2], dp[i][1]+happiness[i][2])
P(max(dp[-1]))

