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
    h,w = LI()
    a = [input() for i in range(h)]
    d = defaultdict(lambda : 0)
    for i in a:
        for j in i:
            d[j] += 1
    l = []
    s = deque()
    for i in d.keys():
        if d[i]&1:
            l.append(i)
        elif d[i]&3:
            s.append(i)
    if len(l) > 1:
        print("No")
        return

    if (h&1) and (w&1):
        if not l:
            print("No")
            return
        d[l[0]] -= 1
        if d[l[0]]&3:
            s.append(l[0])
    n = (h>>1)*(w&1)+(w>>1)*(h&1)
    for i in range(n):
        if not s:
            break
        x = s.pop()
        d[x] -= 2
        if d[x]&3:
            s.append(x)
    if not s:
        print("Yes")
        return
    print("No")
    return


#Solve
if __name__ == "__main__":
    solve()
