import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def bfs(dist, black, H, W):
    q = deque(black)

    res = 0
    while q:
        h, w = q.pop()

        for dh, dw in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W:
                if dist[nh][nw] == -1:
                    dist[nh][nw] = dist[h][w] + 1
                    if res < dist[nh][nw]:
                        res = dist[nh][nw]
                    q.appendleft((nh, nw))

    return res


def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    black = []
    dist = [[-1] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if A[h][w] == "#":
                black.append((h, w))
                dist[h][w] = 0

    ans = bfs(dist, black, H, W)
    print(ans)


if __name__ == "__main__":
    main()
