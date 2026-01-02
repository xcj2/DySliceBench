from collections import deque


def solve(maze, init_y, init_x, H, W):
    distances = [[-1 for _ in range(W)] for _ in range(H)]
    distances[init_y][init_x] = 0

    def is_inside(y, x):
        return 0 <= x < W and 0 <= y < H

    def need_to_search(y, x):
        return maze[y][x] != "#" and distances[y][x] == -1

    four_directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    q = deque()
    q.appendleft([init_y, init_x])

    while q:
        y, x = q.pop()
        d = distances[y][x]

        for dy, dx in four_directions:
            ny, nx = y+dy, x+dx
            if not is_inside(ny, nx):
                continue
            if need_to_search(ny, nx):
                q.appendleft([ny, nx])
                distances[ny][nx] = d+1

    farthest = 0
    for i in range(H):
        for j in range(W):
            # if maze[i][j] != "#":
            farthest = max(farthest, distances[i][j])
    return farthest


def main():
    H, W = map(int, input().split())
    maze = [input() for _ in range(H)]

    farthest = 0
    for i in range(H):
        for j in range(W):
            if maze[i][j] == "#":
                continue
            distance = solve(maze, i, j, H, W)
            farthest = max(distance, farthest)

    print(farthest)


if __name__ == '__main__':
    main()
