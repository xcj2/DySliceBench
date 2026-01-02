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


a = IS()
b = IS()
c = IS()
d = IS()
e = IS()
ryo = [a, b, c, d, e]
ryo = sorted(ryo, key=lambda x:x[-1])[::-1]
least = '10'
for i in ryo:
    if int(least) >= int(i[-1]) and int(i[-1]) != 0:
        least = i[-1]
if least == '10':
    least = '0'
for i in range(len(ryo)):
    if ryo[i][-1] == least:
        number = ryo.pop(i)
        break
for i in range(len(ryo)):
    for j in range(0,140,10):
        if int(ryo[i]) <= j:
            ryo[i] = j
            break
print(sum(ryo) +int(number))
