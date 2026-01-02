#!usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop
import sys
import math
import bisect
import itertools
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return list(sys.stdin.readline())
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007

#C
def C():
    N = I()
    F = LIR(N)
    P = LIR(N)
    ans = -1*float("INF")
    kaiten = list((itertools.product([0,1], repeat=10)))
    del kaiten[0]
    for patern in kaiten:
        i = list(patern)
        anskaiten = [0 for i in range(N)]
        for youbi, n in enumerate(i):
            if n == 1:
                for nn,f in enumerate(F):
                    if f[youbi] == 1:
                        anskaiten[nn] += 1
        ansb = 0
        #print(anskaiten, end="")
        for k, p in enumerate(P):
            ansb += p[anskaiten[k]]
        ans = max(ans, ansb)
    print(ans)
        
if __name__ == '__main__':
    C()


