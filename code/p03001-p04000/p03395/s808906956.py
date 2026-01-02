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
    n = I()
    a = LI()
    b = LI()
    ans = 0
    l = []
    m = 51
    for num in range(1,m+1)[::-1]:
        res = list(range(1,num))+l
        d = [[0 if i == j else float("inf") for j in range(m)] for i in range(m)]
        for k in res:
            for i in range(m):
                d[i][i%k] = 0
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    nd = d[i][k]+d[k][j]
                    if nd < d[i][j]:
                        d[i][j] = nd

        for i in range(n):
            if d[a[i]][b[i]] == float("inf"):
                break
        else:
            continue
        if num == m:
            print(-1)
            return
        else:
            ans += 1<<num
            l.append(num)
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
