#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    n = II()
    a = [7,5,3]
    if n in a:
        print("YES")
    else:
        print("NO")
    return

#B
def B():
    s = S()
    ans = inf
    for i in range(len(s) - 2):
        ans = min(ans, abs(753-int("".join(s[i:i + 3]))))
    print(ans)
    return

#C
def C():
    s = II()
    n = len(str(s))
    ans = 0
    for i in range(3,n+1):
        c = itertools.product(["3", "5", "7"], repeat=i)
        for ci in c:
            if len(set(ci)) < 3:
                continue
            if int("".join(ci)) <= s:
                ans += 1
    print(ans)

        
    return

def primes(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    """ 6以上の数であれば p (素数) <= n のlistを返す """
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k                     // 3::2 * k] = [False] * ((n // 6 - k * k                     // 6 - 1) // k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = [False] * ((n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]
#D
def D():
    n = II()
    primelis = primes(100)
    d = {2: 0, 4: 0, 14: 0, 24: 0, 74: 0}
    for i in primelis:
        b = n
        tmp = 0
        while b // i:
            tmp += (b // i)
            b = (b // i)
        for x in d.keys():
            d[x] += (tmp >= x)
    ans = 0
    ans += (d[2] - 1) * d[24]
    ans += (d[4] - 1) * d[14]
    ans += d[74]
    ans += (d[2] - 2) * (d[4] - 1) * d[4] // 2
    print(ans)
    return

#Solve
if __name__ == '__main__':
    D()
