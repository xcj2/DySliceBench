#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.buffer.readline().split()]
def I(): return int(sys.stdin.buffer.readline())
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
    n,m = LI()
    p = LIR(m)
    d = defaultdict(lambda : -1)
    for i,j in p:
        i -= 1
        if d[i] >= 0 and d[i] != j:
            print(-1)
            return
        d[i] = j
    ans = ""
    for i in range(n):
        if i == 0:
            if d[i] < 0:
                if n == 1:
                    ans += "0"
                else:
                    ans += "1"
            else:
                if d[i] == 0:
                    if n == 1:
                        print(0)
                        return
                    print(-1)
                    return
                ans += str(d[i])
        else:
            if d[i] < 0:
                ans += "0"
            else:
                ans += str(d[i])
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
