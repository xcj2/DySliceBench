import sys
from collections import deque
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


def bfs(H, W, black_cells, dist):
    d = 0
    while black_cells:
        h, w = black_cells.popleft()
        d = dist[h][w]
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            new_h = h + dy
            new_w = w + dx
            if new_h < 0 or H <= new_h or new_w < 0 or W <= new_w:
                continue
            if dist[new_h][new_w] == -1:
                dist[new_h][new_w] = d+1
                black_cells.append((new_h, new_w))
    return d


def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    dist = [[-1]*W for _ in range(H)]

    black_cells = deque()
    for h in range(H):
        for w in range(W):
            if grid[h][w] == '#':
                black_cells.append((h, w))
                dist[h][w] = 0
    print(bfs(H, W, black_cells, dist))


if __name__ == '__main__':
    main()
