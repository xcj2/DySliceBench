#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys, math, bisect, random, itertools
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
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
    if (a + b) % 2:
        print("IMPOSSIBLE")
        return
    print((a + b) // 2)
    return

#B
def B():
    n = II()
    p = LI()
    for i in range(n):
        for k in range(i+1, n):
            pi = p[::1]
            pi[i], pi[k] = pi[k], pi[i]
            for j in range(n-1):
                if pi[j] > pi[j + 1]:
                    break
            else:
                print("YES")
                return
    print("NO")
    return

#C
def C():
    n = II()
    a = LI()
    b = LI()
    ans = 0
    for i in range(n):
        if a[i] >= b[i]:
            ans += b[i]
            continue
        ans += a[i]
        b[i] -= a[i]
        if a[i + 1] >= b[i]:
            ans += b[i]
            a[i + 1] -= b[i]
            continue
        ans += a[i + 1]
        a[i + 1] = 0
    print(ans)
    return

#D
def D():
    s = S()
    s = s[::-1]
    dp = [[0] * 13 for _ in range(len(s))]
    remain = 1
    if s[0] == "?":
        for i in range(10):
            dp[0][i] = 1
    else:
        dp[0][int(s[0])] = 1
    for i in range(1, len(s)):
        remain = (remain * 10) % 13
        dpi = dp[i]
        dpi1 = dp[i-1]
        if s[i] == "?":
            for k in range(10):
                for j in range(13):
                    dpi[(j + remain * k) % 13] += dpi1[j]
                    dpi[(j + remain * k) % 13] %= mod
        else:
            for j in range(13):
                dpi[(j + remain * int(s[i])) % 13] += dpi1[j]
    print(dp[-1][5])
    return

#E
def E():
    return

#F
def F():
    return

#Solve
if __name__ == '__main__':
    A()
