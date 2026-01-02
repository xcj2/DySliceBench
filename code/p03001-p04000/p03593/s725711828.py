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
    h, w = LI()
    x = h & 1 and w & 1
    a = SR(h)
    d = defaultdict(int)
    for i in range(h):
        for j in range(w):
            d[a[i][j]] += 1
    one = 0
    two = 0
    for i in d.values():
        one += i & 1
        two += (i >> 1) & 1
    if x:
        if one == 1:
            if h + w - 2 >= two << 1:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        if one:
            print("No")
        else:
            x = (h & 1) * (w >> 1) + (w & 1) * (h >> 1)
            if x:
                if x >= two:
                    print("Yes")
                else:
                    print("No")
            else:
                if two:
                    print("No")
                else:
                    print("Yes")

    return


#main
if __name__ == '__main__':
    solve()
