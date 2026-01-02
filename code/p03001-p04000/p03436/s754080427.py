import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)

from collections import defaultdict, deque


def initialize_maze(h, w):
    grid = dict()

    for x in range(w + 2):
        grid[(x, 0)] = "#"
        grid[(x, h + 1)] = "#"

    for y in range(h + 2):
        grid[(0, y)] = "#"
        grid[(w + 1, y)] = "#"

    return grid


def main():
    def bfs():
        que = deque()
        que.append((1, 1, 0))

        while que:
            x, y, count = que.popleft()
            for mx, my in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + mx, y + my
                if grid[(nx, ny)] == ".":
                    que.append((nx, ny, count + 1))
                    grid[(nx, ny)] = "!"
                elif grid[(nx, ny)] == "G":
                    min_count = count + 1
                    return min_count
        return - 1

    h, w = map(int, readline().split())
    grid = initialize_maze(h, w)

    black_num = 0
    for y in range(1, h + 1):
        s = input()
        for x, state in enumerate(s, 1):
            grid[(x, y)] = state
            if state == "#":
                black_num += 1

    grid[(w, h)] = "G"

    grid[(1, 1)] = "!"
    min_count = bfs()

    if min_count == -1:
        print(-1)
    else:
        print(h * w - black_num - min_count - 1)


if __name__ == '__main__':
    main()
