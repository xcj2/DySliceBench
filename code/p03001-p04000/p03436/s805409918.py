import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def bfs(maze, H, W, sh, sw, gh, gw):
    visited = [[-1] * W for _ in range(H)]
    visited[sh][sw] = 0

    q = deque([(sh, sw)])

    while q:
        h, w = q.popleft()

        if h == gh and w == gw:
            return visited[gh][gw]

        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W:
                if visited[nh][nw] == -1 and maze[nh][nw] == ".":
                    visited[nh][nw] = visited[h][w] + 1
                    q.append((nh, nw))

    return -1


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    white = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == ".":
                white += 1

    dist = bfs(S, H, W, 0, 0, H - 1, W - 1)
    if dist == -1:
        print(-1)
        return

    ans = white - (dist + 1)
    print(ans)


if __name__ == "__main__":
    main()
