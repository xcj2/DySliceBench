from collections import deque

H, W = [int(s) for s in input().split()]
Ch, Cw = [int(s) - 1 for s in input().split()]
Dh, Dw = [int(s) - 1 for s in input().split()]

fields = [list(input()) for _ in range(H)]
fields_num = [[-1] * W for _ in range(H)]
ok_field = '.'


def get_search_obj(i, j):
    ret = []
    moving_range = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in moving_range:
        if 0 <= i + dx <= (H - 1) and 0 <= j + dy <= (W - 1) and fields[i + dx][j + dy] == ok_field:
            ret.append((i + dx, j + dy))
    return ret


def get_search_obj_cost2(i, j):
    ret = []
    moving_range = ((x, y) for x in range(- 2, 3) for y in range(- 2, 3))
    for dx, dy in moving_range:
        if 0 <= i + dx <= (H - 1) and 0 <= j + dy <= (W - 1) and fields[i + dx][j + dy] == ok_field:
            ret.append((i + dx, j + dy))
    return ret


def bfs(sx, sy):
    start = ((sx, sy), 0)
    dq = deque([start])
    visited = [[False] * W for _ in range(H)]
    while dq:
        (sx, sy), cost = dq.pop()
        if (sx, sy) == (Dh, Dw):
            return cost
        if visited[sx][sy]:
            continue
        else:
            visited[sx][sy] = True
        for x, y in get_search_obj(sx, sy):
            dq.append(((x, y), cost))
        for x, y in get_search_obj_cost2(sx, sy):
            dq.appendleft(((x, y), cost + 1))
    return -1


print(bfs(Ch, Cw))