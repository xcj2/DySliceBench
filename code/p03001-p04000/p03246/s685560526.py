#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007

#A
def A():
    return

#B
def B():
    return

#C
def C():
    n = II()
    v = LI()
    d1 = defaultdict(int)
    d0 = defaultdict(int)
    for num, a in enumerate(v):
        if num % 2:
            d1[a] += 1
        else:
            d0[a] += 1
    A = list(d0.items())
    A.sort(key = lambda x: x[1], reverse = True)
    A = A[:2]
    A.append((0,0))
    B = list(d1.items())
    B.sort(key = lambda x: x[1], reverse = True)
    B = B[:2]
    B.append((0, 0))
    a = n // 2
    b = (n + 1) // 2
    if A[0][0] == B[0][0]:
        ans = min(a - A[0][1] + b - B[1][1], a - A[1][1] + b - B[0][1])
        print(ans)
    else:
        #print(A,B)
        A = A[0][1]
        B = B[0][1]
        print(a+b-A-B)
    return

#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    C()
