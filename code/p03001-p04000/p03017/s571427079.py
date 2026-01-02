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
    n, a, b, c, d = LI_()
    s = S()
    flg = False
    for i in range(a, c-1):
        if s[i] == "#" and s[i + 1] == "#":
            print("No")
            return
    for i in range(b, d-1):
        if s[i] == "#" and s[i + 1] == "#":
            print("No")
            return
    if c > d:
        for i in range(b,d+1):
            if s[i] == "." and s[i + 1] == "." and s[i - 1] == ".":
                flg = True
                break
        if not flg:
            print("No")
            return
    print("Yes")
    return

#B
def B():
    s = S()
    i = len(s) - 1
    state = 0
    ans = 0
    bc = 2
    while i >= 0:
        if state == 0:
            if s[i] == "C":
                state += 1
        elif state == 1:
            if s[i] == "B":
                state += 1
            else:
                state = 0
        elif state == 2:
            if s[i] == "A":
                ans += 1
            elif s[i] == "B":
                state = 0
            else:
                state += 1
        elif state == 3:
            if s[i] == "B":
                state += 1
            elif s[i] == "C":
                state = 1
            else:
                state = 0
        else:
            if s[i] == "A":
                ans += bc
            elif s[i] == "B":
                state = 0
                bc = 2
            else:
                bc += 1
                state = 3
        #print(state,s[i])
        i -= 1
    print(ans)

    return

#C
def C():
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
    A()
