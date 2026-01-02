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
    return

#B
def B():
    return

#C
def C():
    d, g = LI()
    pc = LIR(d)
    g = g // 100
    max_ = 0
    for i in range(d):
        pc[i][1] = pc[i][1] // 100
        max_ = max(pc[i][0], max_)
    dp = [float("INF") for i in range(g+1)]
    skip = [0 for i in range(max_+1)]
    if d >= g:
        print(1)
        return
    dp[0] = 1
    for i in range(d):
        skip[pc[i][0]] = max(skip[pc[i][0]], pc[i][1] + i + 1)
    x = 0
    for k in range(max_+1):
        if x <= skip[k]:
            for i in range(x + 1, skip[k] + 1):
                if i > g:
                    break
                dp[i] = k
            x = skip[k]
    for i in range(d + 1):
        dp[i] = 1
    i = d
    y = d
    while i < g:    
        for x in range(d):
            continue
        
        
     


    
    return

#D
def D():
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
