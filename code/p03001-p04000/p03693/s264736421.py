#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    r,g,b = LI()
    ans = ["YES","NO"]
    print(ans[((((((g<<1)&b)<<1)+((g<<1)^b))&3)>>int(math.log(max(1,(((((g<<1)&b)<<1)+((g<<1)^b))&3)&(-(((((g<<1)&b)<<1)+((g<<1)^b))&3))),2)))&1])
    return

#Solve
if __name__ == "__main__":
    solve()
