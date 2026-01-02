#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    n,m = LI()
    s = input()
    s = s[::-1]
    dp = [float("inf")]*(n+1)
    dp[0] = 0
    q = deque([0])
    ans = []
    f = [0]*(n+1)
    for i in range(n+1):
        if s[i] == "1":
            f[i] = f[i-1]
        else:
            f[i] = i
    while q:
        x = q.popleft()
        r = min(n,x+m)
        y = f[r]
        if x == y:
            break
        dp[y] = dp[x]+1
        q.append(y)
        ans.append(y-x)
    if dp[n] == float("inf"):
        print(-1)
        return
    print(*ans[::-1])
    return

#Solve
if __name__ == "__main__":
    solve()
