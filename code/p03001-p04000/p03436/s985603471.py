#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = SR()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007


#A
def A():
    return

#B
def B():
    return

#C
def C():
    return

#D
def D():
    h,w = LI()
    s = SR(h)
    white = 0
    for i in range(h):
        white += s[i].count(".")
    bfs_map = [[-1 for i in range(w)] for j in range(h)]
    d = [[0,1],[0,-1],[1,0],[-1,0]]
    bfs_map[0][0] = 0
    q = deque()
    q.append([0,0])
    while q:
        y,x = q.popleft()
        for dy,dx in d:
            y_ = y+dy
            x_ = x+dx
            if 0 <= y_ < h and 0 <= x_ < w:
                if s[y_][x_] == "." and bfs_map[y_][x_] < 0:
                    bfs_map[y_][x_] = bfs_map[y][x]+1
                    q.append([y_,x_])
    if bfs_map[h-1][w-1] < 0:
        print(-1)
        quit()
    print(white-1-bfs_map[h-1][w-1])
#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == "__main__":
    D()
