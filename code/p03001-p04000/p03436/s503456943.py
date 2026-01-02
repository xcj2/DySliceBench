from queue import Queue

H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]

def movable(S,vy,vx):
    if 0 <= vy and vy < H and 0 <= vx and vx < W:
        if S[vy][vx] == ".":
            return True
    return False

def bfs(S):
    sy,sx,gy,gx = 0,0,H,W
    Dist = [[None for _ in range(W)] for _ in range(H)]
    vec = [(-1,0),(1,0),(0,-1),(0,1)]
    q = Queue()
    q.put((sy,sx))
    Dist[sy][sx] = 0
    while not q.empty():
        p = q.get()
        py,px = p[0],p[1]
        for vy,vx in vec:
            if movable(S,py+vy,px+vx):
                q.put((py+vy,px+vx))
                Dist[py+vy][px+vx] = Dist[py][px]+1
                S[py+vy][px+vx] = "#"
    return Dist[H-1][W-1]

def white_sum(S):
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                count += 1
    return count

white_sum = white_sum(S)
d_H_W = bfs(S)
if d_H_W == None:
    print(-1)
else:
    print(white_sum - d_H_W - 1)
