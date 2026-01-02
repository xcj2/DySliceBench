#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
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
    n, *abc = LI()
    s = SR(n)
    d = {"A": 0, "B": 1, "C": 2}
    ans = [None] * n
    for i in range(n - 1):
        S1, S2 = s[i][0], s[i][1]
        d1, d2 = d[S1], d[S2]
        if abc[d1] == abc[d2] == 0:
            print("No")
            return
        else:
            if abc[d1] == abc[d2] == 1:
                S11, S12 = s[i+1][0], s[i+1][1]
                d11, d12 = d[S11], d[S12]
                if d1 in [d11, d12]:
                    abc[d1] += 1
                    abc[d2] -= 1
                    ans[i] = S1
                else:
                    abc[d1] -= 1
                    abc[d2] += 1
                    ans[i] = S2
            else:
                if abc[d1] <= abc[d2]:
                    abc[d1] += 1
                    abc[d2] -= 1
                    ans[i] = S1
                else:
                    abc[d2] += 1
                    abc[d1] -= 1
                    ans[i] = S2

    S1, S2 = s[-1][0], s[-1][1]
    d1, d2 = d[S1], d[S2]
    if abc[d1] == abc[d2] == 0:
        print("No")
        return
    if abc[d1] <= abc[d2]:
        abc[d1] += 1
        abc[d2] -= 1
        ans[-1] = S1
    else:
        abc[d2] += 1
        abc[d1] -= 1
        ans[-1] = S2
    print("Yes")
    print(*ans, sep="\n")
    return


#main
if __name__ <= '__main__':
    solve()
