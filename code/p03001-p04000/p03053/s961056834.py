import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def bfs(maze, H, W):
    visited = [[-1] * W for _ in range(H)]
    q = deque([])
    for h in range(H):
        for w in range(W):
            if maze[h][w] == "#":
                visited[h][w] = 0
                q.append((h, w))

    res = 0
    while q:
        h, w = q.popleft()

        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W:
                if visited[nh][nw] == -1 and maze[nh][nw] == ".":
                    visited[nh][nw] = visited[h][w] + 1
                    if res < visited[nh][nw]:
                        res = visited[nh][nw]
                    q.append((nh, nw))

    return res


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = bfs(S, H, W)
    print(ans)


if __name__ == "__main__":
    main()
