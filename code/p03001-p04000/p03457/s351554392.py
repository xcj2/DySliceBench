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
    a, b = LI()
    ans = ['Odd', 'Even']
    print(ans[(a*b)%2-1])
    return

#B
def B():
    a, b = map(str,input().split())
    a = a + b
    if math.sqrt(int(a)).is_integer():
        print("Yes")
    else:
        print("No")
    return

#C
def C():
    n = II()
    pre = (0, 0, 0)
    for _ in range(n):
        t,x,y = LI()
        dist = abs(pre[0] - x) + abs(pre[1] - y)
        if dist <= t - pre[2] and dist % 2 == (t - pre[2]) % 2:
            continue
        print("No")
        return
    print("Yes")
    return

#D
def D():
    return

#Solve
if __name__ == '__main__':
    C()
