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
# dp = [INF] * n
# h = LI()
# dp[0], dp[1] = 0, abs(h[1] - h[0])
# for i in range(2, n):
    # dp[i] = min(dp[i-1] + abs(h[i]-h[i-1]), dp[i])
    # dp[i] = min(dp[i-2] + abs(h[i]-h[i-2]), dp[i])
# P(dp[n-1])
a = II()
b = II()
c = II()
d = II()
e = II()
k = II()
list = sorted([a,b,c,d,e])[::-1]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] - list[j] > k:
            print(':(')
            exit()
print('Yay!')
