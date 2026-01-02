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
    n, k = LI()
    a = LI()
    acc = [0] + list(itertools.accumulate(a))
    lis = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            lis.append(acc[j] - acc[i])
    lis.sort()
    ans = deque()
    for l in lis:
        ans.append(l)
    ansnum = 0
    N = len(bin(acc[-1])) - 2
    for i in range(N):
        tmp = deque()
        lenans = len(ans)
        for _ in range(lenans):
            p = ans.popleft()
            if (1 << (N - 1 - i)) & p:
                ans.append(p)
            else:
                tmp.append(p)
        if len(ans) < k:
            while tmp:
                t = tmp.pop()
                ans.append(t)
        else:
            ansnum |= (1 << (N - 1 - i))
    print(ansnum)
    return


#main
if __name__ == '__main__':
    solve()
