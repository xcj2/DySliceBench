#!/usr/bin/env python3
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
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
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
    a, b, c = LI()
    print(min(a+b,b+c,c+a))
    return

#B
def B():
    def check(s):
        x = len(s)
        if x % 2:
            return False
        if s[:x // 2] == s[x // 2:]:
            return True
    s = S()
    for i in range(1,len(s)):
        if check(s[: - i]):
            print(len(s) - i)
            return

#C
def C():
    II()
    a = LI()
    ans1 = a[-1::-2]
    ans2 = a[-2::-2][::-1]
    ans = ans1 + ans2
    print(*ans)
    return

#D
def D():
    return

#Solve
if __name__ == '__main__':
    C()
