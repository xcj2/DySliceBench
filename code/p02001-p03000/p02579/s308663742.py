import sys
import os
from collections import deque

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")

INF = float("inf")

H,W = LI()
C = LI()
D = LI()
maze = [list(_S()) for i in range(H)]

def bfs():
    # すべてのマスを INF で初期化
    d = [[INF] * W for i in range(H)]
    
    sx = C[0]-1
    sy = C[1]-1
    gx = D[0]-1
    gy = D[1]-1

    # スタート地点をキューに入れ、ワープ数を0にする
    que = deque([])
    que.append((sx, sy))
    d[sx][sy] = 0

    # ワープ対象
    que2 = deque([])

    # 移動4方向のベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # ワープのベクトル
    dx2 = [-2, -2, -2, -2, -2, -1, -1, -1, -1,  0, 0, 1, 1,  1,  1, 2, 2, 2,  2, 2]
    dy2 = [-2, -1,  0,  1,  2, -2, -1,  1,  2, -2, 2, 2, 1, -1, -2, 2, 1, 0, -1, -2]

    while que: 
        while que:
            p = que.popleft()       
            # 取り出してきた状態がゴールなら探索をやめる
            if p[0] == gx and p[1] == gy:
                ans = d[p[0]][p[1]]
                print(ans)
                exit()
            que2.append((p[0], p[1]))
            # 移動4方向をループ
            for i in range(4):
                # 移動した後の点を (nx, ny) とする
                nx = p[0] + dx[i]
                ny = p[1] + dy[i]

                # 移動可否判定、d[nx][ny] == INF であれば訪れたことがない
                if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] != "#" and d[nx][ny] == INF:
                    # 移動できるならキューに入れ、その点のワープ回数を p までのワープ回数で確定する
                    que.append((nx, ny))
                    d[nx][ny] = d[p[0]][p[1]]
                    
        while que2:
            # キューの先頭を取り出す
            p = que2.popleft()
            for i in range(20):
            # for dxi in range(-2,3):
            #     for dyi in range(-2,3):
                nx = p[0] + dx2[i]
                ny = p[1] + dy2[i]
                if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] != "#" and d[nx][ny] == INF:
                    # 移動できるならキューに入れ、その点のワープ回数を p からのワープ回数 +1 で確定する
                    que.append((nx, ny))
                    d[nx][ny] = d[p[0]][p[1]]+1  
        # print('after que2: ',d)  
    return

bfs()
print(-1)