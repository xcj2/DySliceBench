from collections import Counter
from functools import reduce
import bisect
import random
import fractions
import math
# import statistics
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
def GCD_LIST(numbers):  # Greatest Common Divisor
    return reduce(fractions.gcd, numbers)
def LCM_LIST(numbers):  # Least Common Multiple
    return reduce(LCM, numbers)
def LCM(m, n):
    return (m * n // fractions.gcd(m, n))


n, v, c = II(), LI(), LI()
# n = 20
# v = [random.random()* 100 for i in range(20)]
# c = [random.random()* 100 for i in range(20)]
y = 0
maxi = -INF
start = time.time()
for i in range(2 ** n):
    x = 0
    y = 0
    for j in range(n):
        if i >> j & 1:
            x += v[j]
            y += c[j]
    maxi = max(maxi, x - y)

# print(time.time() - start)
print(maxi)
