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
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    h, w, n = LI()
    sr, sc = LI()
    s = S()[::-1]
    t = S()[::-1]
    
    plus = 0
    minus = 1

    def f(l, start, end):
        tmp = [1, end]
        for i in range(n):
            if t[i] == l[plus]:
                tmp[0] -= 1
                tmp[0] = max(tmp[0], 1)
            elif t[i] == l[minus]:
                tmp[1] += 1
                tmp[1] = min(end, tmp[1])
            if s[i] == l[plus]:
                tmp[1] -= 1
            elif s[i] == l[minus]:
                tmp[0] += 1
            if tmp[1] < tmp[0]:
                return False
        return tmp[0] <= start <= tmp[1]
    
    print("YES" if f(["R", "L"], sc, w) and f(["D", "U"], sr, h) else "NO")
    return


#main
if __name__ == '__main__':
    solve()
