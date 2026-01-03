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

#A
def A():
    h,w = LI()
    a = SR(h)
    d = [(1,0),(0,1)]
    bfs = [[1]*w for i in range(h)]
    for y in range(h):
        for x in range(w):
            if a[y][x] == "#":
                bfs[y][x] = 0
                q = deque([(y,x)])
                while q:
                    i,j = q.popleft()
                    k = 0
                    for dy,dx in d:
                        ni = i+dy
                        nj = j+dx
                        if 0 <= ni < h and 0 <= nj < w:
                            if a[ni][nj] == "#":
                                if k:
                                    print("Impossible")
                                    return
                                k = 1
                                bfs[ni][nj] = 0
                                q.append((ni,nj))
                for i in range(h):
                    for j in range(w):
                        if a[i][j] == "#" and bfs[i][j]:
                            print("Impossible")
                            return
                print("Possible")
                return
    return

#B
def B():

    return

#C
def C():

    return

#D
def D():

    return

#E
def E():

    return

#F
def F():

    return

#Solve
if __name__ == "__main__":
    A()
