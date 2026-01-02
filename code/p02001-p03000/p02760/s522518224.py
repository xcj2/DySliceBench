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

#solve
def solve():
    a = LIR(3)
    n = II()
    c = [0] * 9
    for i in range(n):
        b = II()
        for i in range(3):
            for j in range(3):
                c[i * 3 + j] |= a[i][j] == b
    ans = (c[0] & c[1] & c[2]) | (c[3] & c[4] & c[5]) | (c[6] & c[7] & c[8])
    for i in range(3):
        ans |= c[i] & c[3 + i] & c[6 + i]
    ans |= c[0] & c[4] & c[8]
    ans |= c[2] & c[4] & c[6]
    print("Yes" if ans else "No")
    return



#main
if __name__ == '__main__':
    solve()
