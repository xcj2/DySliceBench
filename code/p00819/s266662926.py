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

def solve():
    n = I()
    for i in range(n):
        s = input()
        t = S()
        for k in s[::-1]:
            if k == "J":
                t = [t[-1]]+t[:-1]
            elif k == "C":
                t = t[1:]+[t[0]]
            elif k == "E":
                m = len(t) >> 1
                if len(t)&1:
                    t = t[m+1:]+[t[m]]+t[:m]
                else:
                    t = t[m:]+t[:m]
            elif k == "A":
                t = t[::-1]
            elif k == "M":
                for j in range(len(t)):
                    if t[j].isdecimal():
                        t[j] = str(int(t[j])+1)[-1]
            else:
                for j in range(len(t)):
                    if t[j].isdecimal():
                        if t[j] == "0":
                            t[j] = "9"
                        else:
                            t[j] = str(int(t[j])-1)
        print(*t,sep = "")
    return

#Solve
if __name__ == "__main__":
    solve()

