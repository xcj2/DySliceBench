import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    seen = [[False] * W for _ in range(H)]

    def dfs(sh, sw):
        q = deque([(sh, sw)])
        seen[sh][sw] = True
        black = 0
        white = 0
        if S[sh][sw] == "#":
            black += 1
        else:
            white += 1

        while q:
            h, w = q.popleft()

            for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nh = h + dh
                nw = w + dw

                if 0 <= nh < H and 0 <= nw < W:
                    if seen[nh][nw]:
                        continue
                    if S[h][w] == S[nh][nw]:
                        continue

                    seen[nh][nw] = True
                    q.append((nh, nw))
                    if S[nh][nw] == "#":
                        black += 1
                    else:
                        white += 1

        return black * white

    ans = 0
    for h in range(H):
        for w in range(W):
            if seen[h][w]:
                continue
            ans += dfs(h, w)

    print(ans)


if __name__ == "__main__":
    main()
