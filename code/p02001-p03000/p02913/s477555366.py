#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
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
    d = {"Sunny":1 , "Cloudy":2, "Rainy":0}
    a = ["Sunny", "Cloudy", "Rainy"]
    print(a[d[input().rstrip()]])
    return

#B
def B():
    s = S()
    for i, si in enumerate(s):
        if i % 2:
            if si == "R":
                print("No")
                return
        else:
            if si == "L":
                print("No")
                return
    print("Yes")
    return

#C
def C():
    n, k, q = LI()
    d = [0] * n
    for _ in range(q):
        a = II() - 1
        d[a] += 1
    for a in d:
        if k - (q - a) > 0:
            print("Yes")
        else:
            print("No")
    return

#D
def D():
    n,m = LI()
    a = LI()
    q = []
    for ai in a:
        heappush(q, -ai)
    for _ in range(m):
        heappush(q, heappop(q) / 2)
    ans = 0
    while q:
        ans += int(-heappop(q))
    print(ans)
    return

# E
# 解説AC
# ロリハやZアルゴリズムでもいける
# できないけどDPでできる
def E():
    n = II()
    s = S()
    dp = [[0] * (n + 1) for i in range(n + 1)]
    ans = 0
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if s[i] == s[j]:
                dp[i][j] = max(dp[i][j], dp[i + 1][j + 1] + 1)
            ans = max(ans, min(dp[i][j], j - i))
    print(ans)

    return

#F
def F():
    return

#Solve
if __name__ == '__main__':
    E()
