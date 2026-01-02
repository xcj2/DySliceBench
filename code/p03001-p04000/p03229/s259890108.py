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
    n = II()
    a = IR(n)
    a.sort()
    def f(a):
        q = deque(a)
        p = q.popleft()
        ans = deque([p])
        for i in range(n-1):
            if i % 4 in [2, 3]:
                p = q.popleft()
            else:
                p = q.pop()
            if i & 1:
                ans.appendleft(p)
            else:
                ans.append(p)
        num = 0
        for i in range(n - 1):
            num += abs(ans[i + 1] - ans[i])
        return num
    print(max(f(a), f(a[::-1])))
    return


#main
if __name__ == '__main__':
    solve()
