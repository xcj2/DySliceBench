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
def SR(n): return [input().rstrip()[:-1] for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n = II()
    if n == 0:
        return False
    group = set()
    go_group = set()
    member = set()
    d = defaultdict(int)
    g = SR(n)
    for gi in g:
        group.add(gi.split(":")[0])
        d[gi.split(":")[0]] = gi.split(":")[1].split(",")
    C = defaultdict(int)
    def s(g):
        for gi in g:
            if gi in group:
                if C[gi]:
                    continue
                C[gi] = 1
                s(d[gi])
            else:
                member.add(gi)
    s(d[g[0].split(":")[0]])
    print(len(member))
    return True

#main
if __name__ == '__main__':
    while solve():
        pass

