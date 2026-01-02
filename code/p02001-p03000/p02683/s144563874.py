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
    n,m,x = map(int,input().split())
    s = [list(map(int,input().split())) for i in range(n)]
    ans = float("inf")

    for b in range(1<<n):
        cost = 0
        k = [0]*m
        for i in range(n):
            if b&(1<<i): #i番の本を選んでいたら
                cost += s[i][0] #i番の本の値段を足す
                for j in range(m):
                    k[j] += s[i][j+1] #選んだ本で得られる理解度をトピックごとに合計していく
        if cost < ans and all([i >= x for i in k]):
            ans = cost
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
