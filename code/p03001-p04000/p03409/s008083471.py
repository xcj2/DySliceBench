#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
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
    p = LIR(n)
    q = LIR(n)
    s = [(p[i][0],p[i][1],0) for i in range(n)]+[(q[i][0],q[i][1],1) for i in range(n)]
    s.sort()
    q = []
    ans = 0
    for x,y,i in s:
        if not i:
            q.append(y)
            q.sort()
        else:
            j = bisect.bisect_left(q,y)-1
            if j >= 0:
                q.pop(j)
                ans += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
