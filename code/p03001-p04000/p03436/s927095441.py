import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)

from collections import deque


def initialize_maze(h, w):
    grid = [["."] * (w + 2) for _ in range(h + 2)]

    for row in range(h + 2):
        grid[row][0] = "#"
        grid[row][w + 1] = "#"

    for col in range(w + 2):
        grid[0][col] = "#"
        grid[h + 1][col] = "#"

    return grid


def main():
    def bfs():
        que = deque()
        que.append((1, 1, 0))

        while que:
            row, col, count = que.popleft()
            for mr, mc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr, nc = row + mr, col + mc
                if grid[nr][nc] == ".":
                    que.append((nr, nc, count + 1))
                    grid[nr][nc] = "!"
                elif grid[nr][nc] == "G":
                    min_count = count + 1
                    return min_count
        return - 1

    h, w = map(int, readline().split())
    grid = initialize_maze(h, w)

    black_num = 0
    for row in range(1, h + 1):
        s = input()
        for col, state in enumerate(s, 1):
            grid[row][col] = state
            if state == "#":
                black_num += 1

    grid[h][w] = "G"

    grid[1][1] = "!"
    min_count = bfs()

    if min_count == -1:
        print(-1)
    else:
        print(h * w - black_num - min_count - 1)


if __name__ == '__main__':
    main()
