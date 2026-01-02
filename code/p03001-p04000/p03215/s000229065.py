#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
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
    n,k = LI()
    a = LI()
    s = [0]
    for i in a:
        s.append(s[-1]+i)
    S = []
    for i in range(n):
        for j in range(i+1,n+1):
            S.append(s[j]-s[i])
    ans = 0
    for i in range(max(S).bit_length())[::-1]:
        m = 0
        b = 1<<i
        s_ = []
        for j in S:
            if j&b:
                m += 1
                s_.append(j)
        if len(s_) >= k:
            ans += b
            S = [i for i in s_]
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
