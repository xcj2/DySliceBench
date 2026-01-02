from math import floor,ceil,sqrt,factorial,log
from collections import Counter, deque
from functools import reduce
def S(): return input()
def I(): return int(input())
def MS(): return map(str,input().split())
def MI(): return map(int,input().split())
def LS(): return list(MS())
def LI(): return list(MI())
def LLS(): return [list(map(str, l.split() )) for l in input()]
def LLI(): return [list(map(int, l.split() )) for l in input()]
def LLSN(n: int): return [LS() for _ in range(n)]
def LLIN(n: int): return [LI() for _ in range(n)]

MOD = 10**9 + 7

n, a, b = LI()

def combination(r):
    numerator = reduce(lambda x, y: x * y % MOD, [n - r + i + 1 for i in range(r)])
    denominator = reduce(lambda x, y: x * y % MOD, [i + 1 for i in range(r)])

    return numerator * pow(denominator, MOD-2, MOD) % MOD

ans = pow(2, n, MOD) - 1 - combination(a) - combination(b)

print(ans % MOD)