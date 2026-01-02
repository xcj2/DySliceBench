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
def LS(): return input().split()
def S(): return list(input().rstrip())
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
    s = S()
    t = 0
    l = []
    r = []
    for _ in range(II()):
        q = LS()
        if q[0] == "1":
            t ^= 1
        else:
            _,f, c = q
            if f == "1":
                if t:
                    r.append(c)
                else:
                    l.append(c)
            else:
                if t:
                    l.append(c)
                else:
                    r.append(c)
    if t:
        print("".join(r[::-1] + s[::-1] + l))
    else:
        print("".join(l[::-1] + s + r))
    return


#main
if __name__ == '__main__':
    solve()
