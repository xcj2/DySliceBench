from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    h, w = rl()
    starth, startw = rl()
    endh, endw = rl()
    maze = []
    for i in range(h):
        maze.append(list(input()))

    def nbrs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < h and 0 <= ny and ny < w:
                yield (nx, ny)

    def magic(x, y):
        for nx in range(x - 2, x + 3):
            for ny in range(y - 2, y + 3):
                if nx == x and ny == y: continue
                if 0 <= nx and nx < h and 0 <= ny and ny < w:
                    yield (nx, ny)


    bridges = dd(set)
    def dfs(x, y, num):
        if maze[x][y] != '.':
            return
        else:
            maze[x][y] = num
            for nx, ny in magic(x, y):
                if maze[nx][ny] not in ['.', '#', num]:
                    bridges[num].add(maze[nx][ny])
                    bridges[maze[nx][ny]].add(num)
            for nx, ny in nbrs(x, y):
                dfs(nx, ny, num)

    num = 0
    for x in range(h):
        for y in range(w):
            if maze[x][y] == ".":
                dfs(x, y, num)
                num += 1
   
    curr = [maze[starth-1][startw-1]]
    goal = maze[endh-1][endw-1]
    if curr[0] == goal:
        print (0)
        return

    seen = set(curr)
    depth = 0
    while curr:
        ring = []
        depth += 1
        for node in curr:
            for nxt in bridges[node]:
                if nxt not in seen:
                    if nxt == goal:
                        print (depth)
                        return
                    seen.add(nxt)
                    ring.append(nxt)
        curr = ring

    print (-1)



mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
