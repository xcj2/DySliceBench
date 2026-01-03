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
    n, m = LI()
    x = LI()
    d = defaultdict(int)
    l = [defaultdict(int) for _ in range(m)]
    for a in x: d[a % m] += 1; l[a % m][a] += 1
    ans = 0
    for a in range((m >> 1) + 1):
        if a == m - a or a == 0:
            ans += d[a] >> 1
        else:
            tmp = min(d[a], d[m - a])
            ans += tmp
            if d[a] < d[m - a]:
                tmp = d[m - a] - d[a]
                for value in l[m - a].values():
                    if tmp < 2:
                        break
                    if value >> 1:
                        t = min(tmp >> 1, value >> 1)
                        ans += t
                        tmp -= 2 * t
            else:
                tmp = d[a] - d[m - a]
                for value in l[a].values():
                    if tmp < 2:
                        break
                    if value >> 1:
                        t = min(tmp >> 1, value >> 1)
                        ans += t
                        tmp -= 2 * t
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
