#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
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
    a,b,c,d = map(int,input())
    l = [b,c,d]
    for k in range(1<<3):
        s = a
        ans = []
        for i in range(3):
            if k&(1<<i):
                ans.append("+")
                s += l[i]
            else:
                ans.append("-")
                s -= l[i]
        if s == 7:
            k = [a]
            for i in range(3):
                k.append(ans[i])
                k.append(l[i])
            k.append("=7")
            print(*k,sep="")
            return
    return

#Solve
if __name__ == "__main__":
    solve()
