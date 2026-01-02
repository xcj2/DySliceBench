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
    s = input()
    t = deque()
    for i in s:
        t.append(i)
    q = I()
    k = 0
    for _ in range(q):
        qu = input().split()
        if qu[0] == "1":
            k ^= 1
        else:
            f,c = qu[1:]
            key = (int(f)-1)^k
            if not key:
                t.appendleft(c)
            else:
                t.append(c)
    ans = ""
    if not k:
        while t:
            ans += t.popleft()
    else:
        while t:
            ans += t.pop()
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
