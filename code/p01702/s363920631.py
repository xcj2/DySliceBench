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
def S(): return list(sys.stdin.readline())[:-1]
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

def solve(n,m,q):
    if q == 0:
        if n == 1:
            print("0"*m)
        else:
            print("?"*m)
        return
    ans = ["?"]*m
    f = defaultdict(lambda : "?")
    for i in range(10):
        f[i] = str(i)
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alp)):
        f[i+10] = alp[i]
    s = [[int(x,2) for x in input().split()] for i in range(q)]
    for i in range(q-1):
        s[i+1][0] ^= s[i][0]
    M = (1<<m)-1
    for i in range(n):
        bi = 1<<(n-i-1)
        k = M
        for a,b in s:
            if not a&bi:
                k &= (M-b)
            else:
                k &= b
        for j in range(m):
            if k&(1<<j):
                if ans[-1-j] != "?":
                    ans[-1-j] = 37
                else:
                    ans[-1-j] = i
    ans = [f[i] for i in ans]
    print(*ans,sep = "")
    return

#Solve
if __name__ == "__main__":
    while 1:
        n,m,q = LI()
        if n == 0:
            break
        solve(n,m,q)

