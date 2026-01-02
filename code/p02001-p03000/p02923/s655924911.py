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
def main():
    N = I()
    h = LI()
    lowerRight = [0] * N
    cnt = 0
    for i in range(N-1, 0, -1):
        lowerRight[i] = cnt
        if h[i-1] >= h[i]:
            cnt += 1
        else:
            cnt = 0
    lowerRight[0] = cnt
    print(max(lowerRight))

main()

