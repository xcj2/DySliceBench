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
    h,w = LI()
    a = [input() for i in range(h)]
    d = defaultdict(lambda : 0)
    for i in a:
        for j in i:
            d[j] += 1
    d = list(d.values())
    n = (h>>1)*(w>>1)
    f = [i>>2 for i in d if i >= 4]
    if sum(f) < n:
        print("No")
        return
    fs = [i for i in d if i&1]
    if len(fs) > 1:
        print("No")
        return
    if (h*w)&1:
        if not fs:
            print("No")
            return
    elif fs:
        print("No")
        return
    print("Yes")
    return

#Solve
if __name__ == "__main__":
    solve()
