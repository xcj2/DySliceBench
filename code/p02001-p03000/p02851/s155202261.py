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
    n, k = LI()
    a = LI_()
    ab = a[::1]
    a[0] = a[0] % k
    for i in range(n - 1):
        a[i + 1] = (a[i] + a[i + 1]) % k
    ans = 0
    q = deque([0])
    d = defaultdict(int)
    d[0] += 1
    for x, i in enumerate(a):
        q.append(i)
        if len(q) == k+1:
            x = q.popleft()
            d[x] -= 1
        ans += d[i]
        d[i] += 1
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()