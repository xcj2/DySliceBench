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
    n,p = LI()
    s = list(map(int, input()))
    if p in [2,5]:
        ans = 0
        for i in range(n):
            si = s[i]
            if si%p == 0:
                ans += i+1
        print(ans)
        return
    a = [0]
    k = pow(10,p-2,p)
    K = k
    for i in range(n):
        si = s[i]
        a.append((a[-1]+si*K)%p)
        K *= k
        K %= p
    ans = 0
    d = defaultdict(lambda : 0)
    for i in a:
        ans += d[i]
        d[i] += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
