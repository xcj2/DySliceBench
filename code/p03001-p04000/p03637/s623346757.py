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
    n, m = LI()
    print((n-1)*(m-1))
    return

#B
def B():
    s = S()
    print(s[0]+str(len(s)-2)+s[-1])
    return

#C
def C():
    II()
    a = LI()
    a1 = 0
    a2 = 0
    a3 = 0
    for ai in a:
        if not ai % 4:
            a3 += 1
            continue
        if not ai % 2:
            a2 += 1
            continue
        a1 += 1
    if a2:
        print(["No", "Yes"][a3 >= a1])
        return
    print(["No", "Yes"][a3 >= a1 - 1])
    return
    """
    n, m = LI()
    x = -1
    y = -1
    z = -1
    for i in range(n + 1):
        a = m - 9000 * i - 1000 * n
        if a % 4000 == 0 and a >= 0 and n - i - a / 4000 >= 0:
            y = a / 4000
            z = n - i - y
            x = i
            break
    print(int(x),int(y),int(z))
    """
#D
def D():
    return

#Solve
if __name__ == '__main__':
    C()
