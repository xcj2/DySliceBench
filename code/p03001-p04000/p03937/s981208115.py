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
inf = 1e10

#solve
def solve():
    H, W = LI()
    a = SR(H)
    for h in range(H):
        for w in range(W):
            if a[h][w] == "#":
                t = True
                for mh, mw in [[0, 1], [1, 0]]:
                    mh += h
                    mw += w
                    if 0 <= mh < H and 0 <= mw < W:
                        if a[mh][mw] == "#":
                            if t:
                                t &= False
                            else:
                                print("Impossible")
                                return
                if t and (h != H - 1 and w != W - 1):
                    print("Impossible")
                    return
                t = True
                for mh, mw in [[0, -1], [-1, 0]]:
                    mh += h
                    mw += w
                    if 0 <= mh < H and 0 <= mw < W:
                        if a[mh][mw] == "#":
                            if t:
                                t &= False
                            else:
                                print("Impossible")
                                return
                if t and (h != 0 and w != 0):
                    print("Impossible")
                    return
    print("Possible")
    return


#main
if __name__ == '__main__':
    solve()
