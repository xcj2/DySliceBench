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
alp = [chr(ord('a') + i) for i in range(26)]

#A
def A():
    x, a, b = LI()
    if abs(x - a) > abs(x - b):
        print("B")
    else:
        print("A")
    return

#B
def B():
    s = S()
    s = set(s)
    for i in s:
        alp.remove(i)
    if len(alp) == 0:
        print("None")
    else:
        print(alp[0])
    return

#C
def C():
    n = II()
    a = LI()
    i = 1
    a.sort(reverse=True)
    ans = []
    while i < n:
        if a[i] == a[i - 1]:
            ans.append(a[i])
            if len(ans) == 2:
                print(ans[0] * ans[1])
                return
            i += 2
        else:
            i += 1
    print(0)

#D
def D():
    n = II()
    s1 = S()
    s2 = S()
    i = 0
    f = 0
    if s1[i] == s2[i]:
        ans = 3
        i += 1
        f = 1
    else:
        ans = 6
        i += 2
    while i < n:
        if s1[i] == s2[i]:
            ans *= 2 if f else 1
            ans %= mod
            i += 1
            f = 1
            continue
        i += 2
        ans *= 2 if f else 3
        f = 0
        ans %= mod
    print(ans%mod)
    return

#Solve
if __name__ == '__main__':
    D()
