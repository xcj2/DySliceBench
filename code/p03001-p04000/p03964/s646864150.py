import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def lcm(a, b):
    n = fractions.gcd(a, b)
    return a * b // n

def main():
    N = I()
    curT, curA = 1, 1
    for i in range(N):
        newT, newA = LI()
        # if newT >= curT and newA >= curA:
        #     curT, curA = newT, newA
        #     continue
        r1 = (curT-1)//newT + 1
        r2 = (curA-1)//newA + 1
        curT = newT * max(r1, r2)
        curA = newA * max(r1, r2)
    print(curT + curA)
main()

