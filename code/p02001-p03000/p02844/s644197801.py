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
    s = list(input())
    ans = 0
    f = defaultdict(lambda : [])
    for i in range(n):
        f[s[i]].append(i)
    for t in range(1000):
        k = list(str(t))
        k = ["0"]*(3-len(k))+k
        j = -1
        for i in range(3):
            x = bisect.bisect_right(f[k[i]],j)
            if x >= len(f[k[i]]):
                break
            j = f[k[i]][x]
        else:
            ans += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
