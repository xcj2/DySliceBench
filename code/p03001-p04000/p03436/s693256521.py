import sys
readline = sys.stdin.buffer.readline

from collections import deque
import copy

def myinput():
    return map(int,readline().split())

def mycol(data,col):
    return [ row[col] for row in data ]

h,w = myinput()

maze = [ list(input()) for _ in range(h) ]
# print(maze)

white = 0
black = 0
for i in range(h):
    for j in range(w):
        s = maze[i][j]
        if s==".":
            white += 1
        elif s=="#":
            black += 1
        else:
            pass
# print(white)
# print(black)

def bfs(sy,sx):
    q = deque()
    q.append([sy,sx])
    d = [ [float("inf")]*w for _ in range(h) ]
    d[sy][sx] = 0
    while q:
        y,x = q.popleft()
        if y==(h-1) and x==(w-1):
            break
        else:
            for i,j in ([0,1],[1,0],[-1,0],[0,-1]):
                ny = y + i
                nx = x + j
                if ny==-1 or nx==-1 or ny==h or nx==w:
                    pass
                elif maze[ny][nx]=="#":
                    pass
                elif d[ny][nx]!=float("inf"):
                    pass
                else:
                    d[ny][nx] = d[y][x] + 1
                    q.append([ny,nx])
    return d[h-1][w-1]

path = bfs(0,0)
# print(path)

if path==float("inf"):
    print(-1)
    exit()
else:
    ans = white - ( path + 1 )
    print(ans)
    exit()