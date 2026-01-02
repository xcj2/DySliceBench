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
    n,c,k = LI()
    s = input()
    k += 1
    dpl = [0]*n
    if s[0] == "o":
        dpl[0] = 1
    else:
        dpl[0] = 0
    for i in range(1,n):
        dpl[i] = dpl[i-1]
        if s[i] == "o":
            dpl[i] = max(dpl[i-k]+1,dpl[i])
    dpr = [0]*n
    if s[-1] == "o":
        dpr[-1] = 1
    else:
        dpr[-1] = 0
    for i in range(n-1)[::-1]:
        dpr[i] = dpr[i+1]
        if s[i] == "o":
            dpr[i] = max(dpr[(i+k)%n]+1, dpr[i])
    dpl = [0]+dpl
    dpr += [0]
    ans = []
    for i in range(n):
        if dpl[i]+dpr[i+1] < c:
            print(i+1)
    return

#Solve
if __name__ == "__main__":
    solve()
