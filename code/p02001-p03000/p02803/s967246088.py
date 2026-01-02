import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7

def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return sorted([list(map(int, input().split())) for _ in range(n)])
def graph():
    n=inp()
    g=[[] for _ in range(n)]
    for i in range(n):
        a=inp()
        a-=1
        g[i].append(a)
        g[a].append(i)
    return n,g

def main():
    h, w = map(int, input().split())
    maze = [tuple(input()) for _ in range(h)]
    # h,w = inpm()
    # maze = []
    # for _ in range(h):
    #     s = tuple(input())
    #     maze.append(s)
    ans = 0
    dx = (1,0,-1,0)
    dy = (0,1,0,-1)

    for sx in range(h):
        for sy in range(w):
            if maze[sx][sy] == '#':
                continue
            else:
                d = [[-1 for _ in [0]*w] for _ in [0]*h]
                que = deque()
                d[sx][sy] = 0
                que.append((sx,sy))
                M = 0
                while que:
                    (qx,qy) = que.popleft()
                    for i in range(4):
                        nx=qx+dx[i]
                        ny=qy+dy[i]
                        if nx >= 0 and h>nx and ny>=0 and w>ny and maze[nx][ny]=="." and d[nx][ny]==-1:
                            d[nx][ny]=d[qx][qy]+1
                            if d[qx][qy]+1>M:
                                M= d[qx][qy]+1
                            que.append((nx,ny))
                ans = max(ans,M)
    print(ans)
if __name__ == "__main__":
    main()