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
inf = float("INF")

#solve
def solve():
    h,w,m = LI()
    hw = LIR(m)
    # h, w, m = [3 * 10 ** 5] * 3
    # hw = [(i, i) for i in range(3 * 10 ** 5)]
    dh = defaultdict(int)
    dh1 = defaultdict(int)
    dw = defaultdict(int)
    dw1 = defaultdict(int)
    ma = defaultdict(int)
    for hi, wi in hw:
        dh[hi] += 1
        dw[wi] += 1
        ma[(hi, wi)] = 1
    maxh = max(dh.values())
    maxw = max(dw.values())
    for key, value in dh.items():
        if value == maxh:
            dh1[key] = maxh
    for key, value in dw.items():
        if value == maxw:
            dw1[key] = maxw
    for kh, vh in dh1.items():
        for kw, vw in dw1.items():
            if ma[(kh, kw)] == 0:
                print(vh + vw)
                return
    print(vh + vw - 1)
    
    return


#main
if __name__ == '__main__':
    solve()
