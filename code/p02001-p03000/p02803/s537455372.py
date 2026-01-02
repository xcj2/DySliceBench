import numpy as np
H, W = map(int, input().split())
mp = np.array([list(input()) for _ in range(H)], dtype=str)

import queue
q = queue.Queue()
visit = (mp == "#")

def can_visit(x, y):
    """訪問可能ならTrue。壁、既訪問、世界外ならFalse"""
    if x < 0 or y < 0 or x >= W or y >= H:
        return False
    return not visit[y, x]

def push_neighbor(x, y, d):
    """隣接マスをキューにpush"""
    lis = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    for nx, ny in lis:
        if can_visit(nx, ny):
            q.put((nx, ny, d+1))
            visit[ny, nx] = True

def furthest(sx, sy):
    """位置(sx, sy)から見て一番遠い場所までの距離"""
    # 初期化
    global visit
    visit = (mp == "#")
    if visit[sy, sx]:# 例外処理(スタート地点が壁の中)
        return 0
    visit[sy, sx] = True# 初期位置は訪問済み
    # 計算
    q.put((sx, sy, 0))
    while not q.empty():
        x, y, d = q.get()
        push_neighbor(x, y, d)
    return d

dist = max([furthest(sx, sy) for sx in range(W) for sy in range(H)])
print(dist)