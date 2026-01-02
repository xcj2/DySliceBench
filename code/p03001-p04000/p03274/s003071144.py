import sys
import math
import fractions
from functools import reduce
from collections import Counter
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
def GCD_LIST(numbers):
    return reduce(fractions.gcd, numbers)

N, K = MI()
x = LI()
ans = INF
for i in range(N-K+1):
    ans = min(
            ans,
            abs(x[i]) + abs(x[i+K-1] - x[i]),
            abs(x[i+K-1]) + abs(x[i+K-1] - x[i]))
print(ans)
