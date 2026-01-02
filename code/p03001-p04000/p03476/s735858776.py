#!usr/bin/env python3
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
    m = II()
    print(48-m)
    return

#B
def B():
    a, _ = LI()
    s = S()
    ans = list(map(str, range(10)))
    for num, si in enumerate(s):
        if num != a:
            if si in ans:
                continue
            print("No")
            return
        else:
            if si == "-":
                continue
            print("No")
            return
    print("Yes")
    return

#C
def C():
    n = II()
    csf = LIR(n - 1)
    for i in range(n - 1):
        b = 0
        for k in range(i, n - 1):
            c, s, f = csf[k]
            if b <= s:
                b = s + c
            else:
                b += c + (-b % f)
        print(b)
    print(0)
    return

#D
def D_():
    a = II()
    ans = inf
    b = 0
    for _ in range(1, 10 ** 5):
        b += a
        ans = min(ans, sum(list(map(int, list(str(b))))))
    print(ans)
    return

def D():
    q = II()
    def primes(n):
        """ Input n>=6, Returns a list of primes, 2 <= p < n """
        """ 6以上の数であれば p (素数) <= n のlistを返す """
        n, correction = n-n%6+6, 2-(n%6>1)
        sieve = [True] * (n//3)
        for i in range(1,int(n**0.5)//3+1):
            if sieve[i]:
                k=3*i+1|1
                sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
                sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
        return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]
    primelis = primes(10 ** 5)
    d = defaultdict(int)
    for i in primelis:
        d[i] += 1
    dp = [0]
    for i in range(3, 10 ** 5, 2):
        dp.append(dp[-1] + (1 if (d[i] and d[(i + 1) // 2]) else 0))
    for i in range(q):
        l, r = map(lambda x: x // 2, LI())
        if l == 0:
            print(dp[r])
            continue
        print(dp[r] - dp[l - 1])



#Solve
if __name__ == '__main__':
    D()
