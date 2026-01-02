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
    s1 = list(input())
    rev1 = s1[::-1]
    n = len(s1)
    s2 = s1[0:(n-1)//2]
    rev2 = s2[::-1]
    s3 = s1[(n+3)//2-1:n]
    rev3 = s3[::-1]
    if s1 == rev1 and s2 == rev2 and s3 == rev3:
        print("Yes")
    else:
        print("No")

    return

#Solve
if __name__ == "__main__":
    solve()