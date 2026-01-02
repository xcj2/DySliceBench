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
inf = float('INF')

#A
def A():
    b = S()
    b = b[0]
    if b == "A":
        print("T")
    elif b == "T":
        print("A")
    elif b == "C":
        print("G")
    elif b == "G":
        print("C")
    return

#B
def B():
    s = S()
    agct = ["A", "G", "C", "T"]
    ans = 0
    for num, i in enumerate(s):
        ansb = 0
        if i in agct:
            ansb += 1
            for k in range(num+1, len(s)):
                if s[k] in agct:
                    ansb += 1
                else:
                    break
        ans = max(ans, ansb)
    print(ans)
    return

#C
def C():
    n, q = LI()
    s = S()
    ans = [0 for i in range(n+1)]
    ac = 0
    for num, ss in enumerate(s):
        if (not ac) and ss == "A":
            ac = 1
            ans[num] = ans[num - 1]
        elif ac and ss == "C":
            ac = 0
            ans[num] = ans[num - 1] + 1
        else:
            if ss == "A":
                ac = 1
            else:
                ac = 0
            ans[num] = ans[num - 1]
    lr = LIR_(q)
    for l,r in lr:
        print(ans[r]-ans[l])

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
