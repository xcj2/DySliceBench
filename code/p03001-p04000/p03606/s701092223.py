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
    s = S()
    if "9" in s:
        print("Yes")
    else:
        print("No")
    return

#B
def B():
    n = II()
    ans = 0
    for i in range(n):
        l, r = LI()
        ans += r - l + 1
    print(ans)
    return

#C
def C():
    n = II()
    A = {}
    for _ in range(n):
        k = II()
        if not k in A:
            A[k] = 1
        else:
            A[k] += 1
    ans = 0
    for item in A.values():
        ans += item % 2
    print(ans)
    return

#D
def D():
    return

#Solve
if __name__ == '__main__':
    B()