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
    a, b, c, d, e, f = LI()
    lis = []
    for i in range(f //c + 1):
        for k in range(f // d + 1):
            lis.append(c * i + d * k)
    lis = list(set(lis))
    lis.sort()
    ans = [100 * a, 0]
    for i in range(f // 100 + 1):
        for k in range(f // 100 + 1):
            if i == k == 0:
                continue
            water = a * i + b * k
            if water * 100 > f:
                continue
            E = min(f - water * 100, water * e)
            if E <= 0:
                continue
            aa = bisect_right(lis, E) - 1
            if aa == -1:
                continue
            aa = lis[aa]
            if ans[1] / ans[0] < aa / (water * 100 + aa):
                ans = [water * 100 + aa, aa]
    print(*ans)

    return


#main
if __name__ == '__main__':
    solve()
