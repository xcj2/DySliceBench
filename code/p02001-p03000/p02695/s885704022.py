#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
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
    def f(A):
        res = 0
        for a,b,c,d in g:
            if A[b] == A[a]+c:
                res += d
        return res
    N,M,Q = map(int,input().split())
    g = [list(map(int,input().split())) for i in range(Q)]
    #g[i][0] == ai
    for i in range(Q):
        g[i][0] -= 1  #ai -= 1
        g[i][1] -= 1  #bi -= 1
    l = [([i],i) for i in range(1,M+1)]  #[([1],1),([2],2),....,([M],M)]
    for i in range(N-1): #1個目の要素にN桁の数列を生成
        l = [(x+[j], j) for (x,y) in l for j in range(y,M+1)]
    ans = 0
    for A,_ in l:
        s = f(A)
        if ans < s:
            ans = s #得点の最大値を厳選
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
