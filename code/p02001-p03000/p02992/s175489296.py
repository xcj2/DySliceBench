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
sqrt = math.sqrt
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
    s = S()
    b = list(set(s))
    a = len(list(set(s)))
    if a == 2 and s.count(b[0]) == s.count(b[1]) == 2:
        print("Yes")
    else:
        print("No")
    return

#B
def B():
    n = II()
    p = LI()
    ans = 0
    for i in range(1,n-1):
        if (p[i - 1] < p[i] and p[i] < p[i + 1]) or (p[i + 1] < p[i] and p[i] < p[i - 1]):
            ans += 1
    print(ans)
    return

#C
def C():
    n = II()
    d = LI()
    d.sort()
    ans = 0
    for i in range(10**5+1):
        if n // 2 == bisect_left(d, i):
            ans += 1
    print(ans)
    return


def combination_mod(n, k, mod):
    # power_funcを用いて(nCk) mod p を求める 
    # nCk = n!/((n-k)!k!)を使用

    from math import factorial
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    a = factorial(n) % mod
    b = factorial(k) % mod
    c = factorial(n - k) % mod
    return (a * power_func(b, mod - 2, mod) * power_func(c, mod - 2, mod)) % mod
    
def power_func(a, b, mod):
    # a^b mod p を求める
    # bを2進数分解して高速累乗

    if b == 0: return 1
    if b % 2 == 0:
        d = power_func(a, b // 2, mod)
        return d * d % mod
    if b % 2 == 1:
        return (a * power_func(a, b - 1, mod)) % mod

#D
def D():
    n, k = LI()
    ans = 0
    for i in range(1,k+1):
        a = combination_mod(n - k + 1, i, mod)
        b = combination_mod(k - 1, i - 1, mod)
        print((a*b)%mod)
    return

def dijkstra(num, start, edge, g):

    dist = defaultdict(lambda: inf)
    dist[(start,0)] = 0
    q = [(dist[(start,0)], start, 0)]
    while q:
        du, u, t = heappop(q)
        for j in edge[u]:
            if t == 2:
                t = -1
            if dist[(j, t + 1)] > du + 1:
                dist[(j, t + 1)] = du + 1
                heappush(q, [dist[(j, t + 1)], j, t + 1])
    return dist
#E
def E():
    n, m = LI()
    v = LIR_(m)
    s, t = LI_()
    edge = defaultdict(list)
    for x,y in v:
        edge[x].append(y)
    d = dijkstra(n, s, edge, t)
    if d[(t,0)] == inf:
        print(-1)
    else:
        print(d[(t,0)]//3)
    return

# F
# 解説AC
# √nまでで約数の全列挙ができるということは
# n <= a * b (a <= bとしたときに)
# 各 a は √nまでしかないことはわかる
# ( a > √n なら b < √n だからね)
# すると各aに対して対応するbの最大値が存在するため
# b の個数は高々 √n 個しか無いことがわかる
# 後はDPでどうぞ 
def F():
    n, k = LI()
    f = defaultdict(int)
    Range = int(sqrt(n))
    dp = [0] * (2 * Range)
    m = 0
    l = 0
    for i in range(Range, 0, -1):
        dp[i - 1] = 1
        f[i - 1] = 1
        if n // i == i:
            l = 1
            continue
        dp[Range + m] = n // i - n // (i + 1)
        f[Range + m] = n // i - n // (i + 1)
        m += 1
    R = 2 * Range - l
    for _ in range(k - 1):
        ndp = [0] * (2 * Range)
        for j in range(R):
            ndp[R - j - 1] = dp[j]
        ndp = list(itertools.accumulate(ndp[::-1]))[::-1]
        dp = [(d * f[num]) % mod for num,d in enumerate(ndp)]
    ans = sum(dp)%mod
    print(ans)
    return



#Solve
if __name__ == '__main__':
    F()
