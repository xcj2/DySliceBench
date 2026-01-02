from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce, lru_cache
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def MAP1()  : return map(lambda x:int(x)-1,input().split())
def LIST()  : return list(MAP())
def LIST1() : return list(MAP1())

def bfs():
    d = [[inf]*w for i in range(h)]

    dy_dx0 = [[0,1],[1,0],[0,-1],[-1,0]] 
    dy_dx1 = [[2,2],[2,1],[2,0],[2,-1],[2,-2],[1,2],[1,1],[1,-1],[1,-2],[0,2],[0,-2],[-1,2],[-1,1],[-1,-1],[-1,-2],[-2,2],[-2,1],[-2,0],[-2,-1],[-2,-2]]

    que = deque([])
    que.append((sy, sx))
    d[sy][sx] = 0
 
    while que:
        p = que.popleft()
        if p[0] == gy and p[1] == gx:
            break
        for i in range(4):
            ny = p[0] + dy_dx0[i][0]
            nx = p[1] + dy_dx0[i][1]
 
            if 0 <= ny < h and 0 <= nx < w and s[ny][nx] != '#' and d[ny][nx] > d[p[0]][p[1]]:
                que.appendleft((ny,nx))
                d[ny][nx] = d[p[0]][p[1]]

        for i in range(20):
            ny = p[0] + dy_dx1[i][0]
            nx = p[1] + dy_dx1[i][1]
 
            if 0 <= ny < h and 0 <= nx < w and s[ny][nx] != '#' and d[ny][nx] == inf:
                que.append((ny,nx))
                d[ny][nx] = d[p[0]][p[1]] + 1 
 
    return d[gy][gx]

h, w = MAP()
sy, sx = MAP1()
gy, gx = MAP1()
s = [input() for _ in range(h)]
ans = bfs()
if ans == inf:
    print(-1)
else:
    print(ans)
