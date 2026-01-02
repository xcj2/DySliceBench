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

#A
def A():
    r = II()
    if r < 1200:
        print("ABC")
    elif r < 2800:
        print("ARC")
    else:
        print("AGC")
    return

#B
def B():
    return

#C
def C():
    d, g = LI()
    pc = LIR(d)
    ans = float("INF")
    tokumono = list(itertools.product((0, 1), repeat=d))
    for toku in tokumono:
        ansa = 0
        ansb = 0
        for i in range(len(toku)):
            if toku[i] == 1:
                ansa += pc[i][0]
                ansb += pc[i][0] * (i + 1) * 100 + pc[i][1]
        for k in range(len(toku) - 1, -1, -1):
            if toku[k] == 0:
                for i in range(pc[k][0] + 1):
                    if i == pc[k][0]:
                        ansb += pc[k][1]
                    if ansb >= g:
                        ans = min(ans, ansa)
                        break
                    ansa += 1
                    ansb += (k+1) * 100
                break
    print(ans)
    return

#D ? 
def D_():
    N, X = LI()
    def dfs(n, x):
        #print(n, x)
        if x == 1 and n > 0:
            return 0 
        elif x < 2 ** (n + 1) - 1:
            return dfs(n - 1, x - 1)
        elif x == 2 ** (n + 1) - 1:
            return 2 ** n 
        elif x == 2 ** (n + 2) - 3:
            return 2 ** (n + 1) - 1
        else:
            return dfs(n - 1, x - 2 ** (n + 1) + 1) + 2 ** n 
    a = dfs(N, X)
    print(a)
    return

def D():
    s = S()
    dp = [0] * 3
    s = s[::-1]
    x = 1
    for i, si in enumerate(s):
        if si == "A":
            dp[0] = (dp[0] + dp[1]) % mod
        elif si == "B":
            dp[1] = (dp[1] + dp[2]) % mod
        elif si == "C":
            dp[2] = (dp[2] + x) % mod
        else:
            dp[0] = (dp[0] * 3 + dp[1]) % mod
            dp[1] = (dp[1] * 3 + dp[2]) % mod
            dp[2] = (dp[2] * 3 + x) % mod
            x *= 3
            x %= mod
    print(dp[0])

#Solve
if __name__ == '__main__':
    D()
