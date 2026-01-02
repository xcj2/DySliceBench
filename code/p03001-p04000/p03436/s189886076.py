def debug_print(maze):
    for xx in maze:
        print(xx)
#        for yy in xx:
#            print(yy)

def clear_maze(h,w,sx, sy, gx, gy, maze):
#    debug_print(maze)
    INF = 100000000
    distance = [[INF for _ in range(w)] for _ in range(h)]
    def bfs():
        queue = []
        queue.insert(0, (sy, sx))
        distance[sy][sx] = 0
        while len(queue):
            y, x = queue.pop()
            if x == gx and y == gy:
                break
            for i in range(0, 4):
                nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]
                if (0<= nx <w and 0<= ny <h and maze[ny][nx] != '#' and distance[ny][nx] == INF):
                    queue.insert(0, (ny, nx))
                    distance[ny][nx] = distance[y][x] + 1
        return distance[gy][gx]
    return bfs()
###########################################

import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')

H, W = LI()
cur = int(0)
S = [list(str(input().rstrip('\n'))) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            cur +=1
#print (clear_maze(H,W,0,0,W-1,H-1,S))
ans = H*W - (clear_maze(H,W,0,0,W-1,H-1,S) + 1 + cur)
if ans<0:
    ans = -1
print(ans)