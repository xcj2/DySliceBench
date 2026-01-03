import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


def main():
    N, M = map(int, input().split())
    S = []

    d = [[float("inf")] * N for _ in range(N)]
    L = []
    for i in range(M):
        a, b, c = map(int, input().split())
        d[a - 1][b - 1] = c
        d[b - 1][a - 1] = c
        if a < b:
            L.append((a - 1, b - 1))
        else:
            L.append((b - 1, a - 1))
    for i in range(N):
        d[i][i] = 0
    L = set(L)

    def warshall_floyd(d):
        # d[i][j]: iからjへの最短距離
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if d[i][j] > d[i][k] + d[k][j]:
                        d[i][j] = d[i][k] + d[k][j]
                        if i < j:
                            if (i, j) in L:
                                S.append((i, j))
                        else:
                            if (j, i) in L:
                                S.append((j, i))
        return d

    warshall_floyd(d)
    print(len(set(S)))


if __name__ == "__main__":
    main()
