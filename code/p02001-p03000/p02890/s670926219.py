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
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
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
    n = I()
    a = LI()
    d = defaultdict(lambda : 0)
    for i in a:
        d[i] += 1
    d = list(d.values())
    q = []
    for i in d:
        heappush(q,i)
    ans = []
    for k in range(n):
        if not q:
            break
        else:
            x = heappop(q)
            ans.append(x)
            while q and x:
                y = heappop(q)
                y += 1
                x -= 1
                heappush(q,y)
    for i in ans[::-1]+[0]*(n-len(ans)):
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()
