import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def warshall_floyd(n, d):
    # d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def main():
    N = int(input())
    S = [list(input()) for _ in range(N)]

    def bfs(start, S):
        visited = [False] * N
        visited[start] = True
        group = [-1] * N
        group[start] = 0
        q = deque([(start, 0)])
        while q:
            n, g = q.popleft()

            for i in range(N):
                if S[n][i] == "1":
                    if visited[i]:
                        if abs(group[i] - g) != 1:
                            return -1
                        else:
                            continue
                    else:
                        group[i] = g + 1
                        visited[i] = True
                        q.append((i, g + 1))
                else:
                    continue
        n_group = 1
        for i in range(N):
            if group[i] == -1:
                return -1
            if n_group < group[i] + 1:
                n_group = group[i] + 1
        return n_group

    answer = -1
    for i in range(N):
        n_group = bfs(i, S)
        if n_group > answer:
            answer = n_group
    print(answer)


if __name__ == "__main__":
    main()
