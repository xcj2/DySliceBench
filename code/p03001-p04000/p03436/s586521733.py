from collections import deque
import sys
sys.setrecursionlimit(4000)

def validCordinate(x, y, dist, Grid):
    if x < 0 or x >= len(Grid[0]):
        return False
    if y < 0 or y >= len(Grid):
        return False

    if dist[y][x] != -1:
        return False

    if Grid[y][x] != '.':
        return False

    return True

def bfs(x, y, q, dist, Grid):
    # 隣接点を検証
    if validCordinate(x + 1, y, dist, Grid):
        q.append((x+1, y))
        dist[y][x+1] = dist[y][x] + 1
    if validCordinate(x, y + 1, dist, Grid):
        q.append((x, y + 1))
        dist[y+1][x] = dist[y][x] + 1
    if validCordinate(x - 1, y, dist, Grid):
        q.append((x-1, y))
        dist[y][x-1] = dist[y][x] + 1
    if validCordinate(x, y - 1, dist, Grid):
        q.append((x, y-1))
        dist[y-1][x] = dist[y][x] + 1


    # finish
    if x == len(Grid[0]) - 1 and y == len(Grid) - 1:
        return dist
    if len(q) == 0:
        return False

    cx, cy = q.popleft()

    return bfs(cx, cy, q, dist, Grid)
    

def main():
    # input
    H, W = map(int, input().split())
    Grid = []
    dist = [[-1 for j in range(W)] for i in range(H)]
    q = deque()

    for i in range(H):
       Grid.append(input()) 


    dist[0][0] = 0
    res = bfs(0, 0, q, dist, Grid)

    if res:
        whiteNumber = 0
        for i in range(H):
            for j in range(W):
                if Grid[i][j] == ".":
                    whiteNumber += 1
        print(whiteNumber - res[-1][-1] - 1)
    else:
        print(-1)

if __name__ == "__main__":
    main()