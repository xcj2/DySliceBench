'''''''''''''''''''''
grid[h][w]

    w=0 w=1 w=2
h=0
h=1
h=2
'''''''''''''''''''''

from collections import deque
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]     # 動ける場所の候補


def debug(start, goal, p, t):
    player = p
    debug_grid = list(list(grid[h]) for h in range(H))
    if start != (None, None):
        debug_grid[start[0]][start[1]] = "S"
    if goal != (None, None):
        debug_grid[goal[0]][goal[1]] = "G"
    debug_grid[player[0]][player[1]] = "P"
    print("~~~~~~~~~ t = " + str(t+1) + "  ~~~~~~~~")
    for debug_h in range(H):
        print("".join(str(debug_grid[debug_h][debug_w]) for debug_w in range(W)))


def distance_list(grid, visit, start, goal=(None,None)):
    dist = [[-1] * W for _ in range(H)]
    dist[start[0]][start[1]] = 0
    visit[start[0]][start[1]] = 1
    next_set = deque([(start, 0)])
    while next_set:
        p, t = next_set.popleft()
        h, w = p
        for dh, dw in move:
            q = (h + dh, w + dw)
            if q[0] < 0 or q[0] >= H or q[1] < 0 or q[1] >= W:
                continue
            if grid[q[0]][q[1]] == wall:
                continue
            if visit[q[0]][q[1]] == 1:
                continue
            #### (debug code) ######
            # debug(start, goal, q, t)
            ########################
            if q == goal:
                return t + 1
            visit[q[0]][q[1]] = 1
            dist[q[0]][q[1]] = t+1
            next_set.append((q, t + 1))
    return dist


def most_distant_point(grid, visit, start=(0,0)):
    res = (start, 0)
    temp = 0
    dist = distance_list(grid, visit, start)
    for h in range(H):
        for w in range(W):
            if dist[h][w] > temp:
                temp = dist[h][w]
                res = ((h,w), temp)
    return res


def diameter(grid, visit, start=(0,0)):
    visit = [[0] * W for _ in range(H)]
    p = most_distant_point(grid, visit, start)
    visit = [[0]*W for _ in range(H)]
    res = most_distant_point(grid, visit, start=p[0])
    return res[1]


def diameter2(grid):
    res = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == road and visit[h][w] == 0:
                temp = diameter(grid, visit, (h,w))
                if temp > res:
                    res =temp
    return res

############################################################################################


######################################################
# スタート地点がinputで与えられる場合 (h軸とw軸の反転に注意)
######################################################

road, wall = ".", "#"                         # (進行可能を意味する記号, 進行不可を意味する記号)

H,W = map(int,input().split())                # 左上は(h,w)=(0,0)、右下は(h,w)=(H-1,W-1)

grid = []
for h in range(H):
    grid.append(input().rstrip())                # 文字列を読み込むと改行が入るため、rstrip()で消す

visit = [[0]*W for _ in range(H)]
res = diameter2(grid)           #  visitを初期化せずに何度も呼び出すと、visit が変わって返り値も変わるので注意

print(res)
