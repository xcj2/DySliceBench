import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
# from collections import Counter,defaultdict,deque
# from itertools import permutations, combinations
# from heapq import heappop, heappush
# input = sys.stdin.readline
# sys.setrecursionlimit(10**8)
# mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

h,w = inpm()
maze = inplL(h)

ans = 0
for sh in range(h):
    for sw in range(w):
        if maze[sh][sw] == '#':
            continue

        q = queue.Queue()
        q.put((sh,sw,0))

        field = [[-1]*w for i in range(h)]
        tmp = 0
        while not q.empty():
            yy,xx,kk = q.get()
            if field[yy][xx] >= 0: continue

            field[yy][xx] = kk
            if tmp < kk:
                gh,gw = (yy,xx)
                tmp = kk
            if yy != h-1 and maze[yy+1][xx] == '.':
                q.put((yy+1,xx,kk+1))
            if xx != w-1 and  maze[yy][xx+1] == '.':
                q.put((yy,xx+1,kk+1))
            if yy != 0 and  maze[yy-1][xx] == '.':
                q.put((yy-1,xx,kk+1))
            if xx != 0 and  maze[yy][xx-1] == '.':
                q.put((yy,xx-1,kk+1))
        ans = max(ans,field[gh][gw])

print(ans)