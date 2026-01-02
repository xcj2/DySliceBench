# coding: utf-8
import sys
from heapq import heapify, heappop, heappush

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

H, W, K = lr()
SX, SY, GX, GY = lr()
SX -= 1; SY -= 1; GX -= 1; GY -= 1
pond = [sr() for _ in range(H)]
INF = 10 ** 10

def to_ID(x, y, con):
    return (x*W + y) * 4 + con

def mod_ceil_K(x):
    return (x+K-1) // K * K

def push(d, id):
    if dist[id] < d:
        return
    dist[id] = d
    heappush(que, (d, id))    

dist = [INF] * (H*W*4)
start = to_ID(SX, SY, 0)
dist[start] = 0
que = [(0, start)]
UDLR = [(0, -1), (1, 0), (0, 1), (-1, 0)]
goal = to_ID(GX, GY, 0)
while que:
    d, id = heappop(que)
    if id == goal:
        answer = mod_ceil_K(d) // K
        print(answer); exit()
    if dist[id] < d:
        continue
    x = id // 4 // W
    y = id // 4 % W
    con = id % 4
    for i in range(4):
        next_id = to_ID(x, y, i)
        if dist[next_id] > mod_ceil_K(d):
            push(mod_ceil_K(d), next_id)
    dx = UDLR[con][0]; dy = UDLR[con][1]
    nx = x + dx; ny = y + dy
    if not (0 <= nx < H and 0 <= ny < W) or pond[nx][ny] == '@':
        continue
    next_id = to_ID(nx, ny, con)
    if dist[next_id] > d + 1:
        dist[next_id] = d + 1
        push(d+1, next_id)
    
print(-1)