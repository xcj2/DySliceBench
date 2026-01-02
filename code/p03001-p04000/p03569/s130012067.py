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
    s = S()
    sa = s[::1]
    sa = sa.replace("x", "")
    for i in range(len(sa)):
        if sa[i] == sa[-i - 1]:
            continue
        print(-1)
        return
    ans = 0
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
            continue
        ans += 1
        if s[i] == "x":
            i += 1
        if s[j] == "x":
            j -= 1
    print(ans)



    return


#main
if __name__ == '__main__':
    solve()
