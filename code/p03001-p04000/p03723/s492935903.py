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
    a, b, c = LI()
    d = defaultdict(int)
    d[(a, b, c)] = 1
    ans = 0
    while 1:
        if a & 1 or b & 1 or c & 1: break
        a, b, c = (b + c) // 2, (a + c) // 2, (a + b) // 2
        ans += 1
        if d[(a, b, c)]:
            print(-1)
            return
        d[(a, b, c)] = 1
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
