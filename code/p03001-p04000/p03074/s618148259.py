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
    a, b = LI()
    if a < b:
        a, b = b, a
    ans = a
    a -= 1
    ans += max(a, b)
    print(ans)
    return

#B
def B():
    n = II()
    h = LI()
    dp = [0 for i in range(n)]
    ans = 0
    for i in range(n):
        dp[i] = max(dp[i - 1], h[i])
        if dp[i - 1] <= h[i]:
            ans += 1
    print(ans)
    return

#C
def C():
    s = S()
    ans = 0
    for num, i in enumerate(s):
        if num % 2:
            if i == "0":
                ans += 1
        else:
            if i == "1":
                ans += 1
    ansb = 0
    for num, i in enumerate(s):
        if not num % 2:
            if i == "0":
                ansb += 1
        else:
            if i == "1":
                ansb += 1
    print(min(ans, ansb))
    return

#D
def D():
    n, K = LI()
    s = S()
    ans = []
    i = 0
    while i < n:
        l = 1
        for x in range(i+1, n):
            if s[x] == s[i]:
                l = x + 1 - i
                continue
            l = x - i
            break
        ans.append(l)
        i += l
    f = 0
    if s[-1] == "0":
        ans.append(0)
        f = 1
    
    dp = [0 for i in range(len(ans))]
    #print(ans)    
    if s[0] == "0":
        i = 2*K
        dp[0] = sum(ans[:i])
        a = 1
    if s[0] == "1":
        i = 2*K+1
        dp[0] = sum(ans[:i])
        a = 0
    x = 1
    while x + 2 * K < len(ans):
        if not a:
            dp[x] = dp[x - 1] - ans[x-1]
        else:
            dp[x] = dp[x - 1] + ans[x + 2 * K] + ans[x+2*K-1] - ans[x-1]
        x += 1
        a = (a + 1) % 2
        
    print(max(dp))
        

    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    D()
