import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys
import copy

sys.setrecursionlimit(10**9)
mod = 998244353
inf = 10**20

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


H,W = LI()
field = [list(input()) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if field[i][j]==".":
            field[i][j]=inf

tmp = copy.deepcopy(field)

dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans=[]


def bfs(sh,sw):
    field[sh][sw] = 0
    que = collections.deque([[sh,sw]])

    while que:
        h,w = que.popleft()
        for i in range(4):
            nh = h+dx[i]
            nw = w+dy[i]
            if (nh<0) or (nw<0) or (nw>W-1) or (nh>H-1):
                continue
            dist = field[nh][nw]
            if dist!="#":
                if dist>field[h][w]+1:
                    field[nh][nw] = field[h][w]+1
                    que.append([nh,nw])

    m = 0
    for i in range(H):
        for j in range(W):
            if field[i][j]!="#":
                if field[i][j]>m:
                    m = field[i][j]
    return m

for i in range(H):
    for j in range(W):
        field = copy.deepcopy(tmp)
        if field[i][j]=="#":
            continue
        ans.append(bfs(i,j))


print(max(ans))