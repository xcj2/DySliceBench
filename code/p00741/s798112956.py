from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

dx = [1,1,1,0,0,0,-1,-1,-1]
dy = [1,0,-1,1,0,-1,1,0,-1]

def dfs(x,y):
    global MAP
    if MAP[y][x] == 0:
        return
    else:
        MAP[y][x] = 0
        for i in range(9):
            dfs(x+dx[i],y+dy[i])


while True:
    W,H = inpl()
    if W == 0:
        break
    else:
        MAP = [[0] + inpl() + [0] for i in range(H)]
        MAP = [[0]*(W+2)] + MAP + [[0]*(W+2)]
        ans = 0
        for y in range(1,H+1):
            for x in range(1,W+1):
                if MAP[y][x] == 1:
                    ans += 1
                    dfs(x,y)
        print(ans)

