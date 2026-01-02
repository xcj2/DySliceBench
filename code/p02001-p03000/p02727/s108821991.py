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
    x,y,a,b,c = LI()
    p = LI()
    q = LI()
    r = LI()
    s = [(i,0) for i in p]+[(i,1) for i in q]+[(i,2) for i in r]
    s.sort(reverse = True)
    ans = 0
    f = [0,0]
    l = [x,y]
    q = deque()
    q2 = deque()
    for a,i in s:
        if i > 1:
            q.append(a)
        else:
            if f[i] < l[i]:
                ans += a
                f[i] += 1
                q2.append(a)
    s = ans
    while q and q2:
        s -= q2.pop()
        s += q.popleft()
        if ans < s:
            ans = s
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
