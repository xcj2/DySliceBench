import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)
MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    seen = [[False] * W for _ in range(H)]
    black = [0]
    white = [0]

    def dfs(x, y):
        seen[x][y] = True
        if S[x][y] == "#":
            black[-1] += 1
        else:
            white[-1] += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < H and 0 <= ny < W):
                continue
            if S[x][y] == S[nx][ny]:
                continue
            if seen[nx][ny]:
                continue
            dfs(nx, ny)

    answer = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == ".":
                continue
            if seen[h][w]:
                continue
            black.append(0)
            white.append(0)
            dfs(h, w)

    for i in range(len(black)):
        answer += black[i] * white[i]
    print(answer)


if __name__ == "__main__":
    main()
