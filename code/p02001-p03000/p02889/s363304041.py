import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def read_into(*A):
    for a, v in zip(A, read_ints()):
        a.append(v)


def solve():
    N, M, L = read_ints()
    dist = [
        [math.inf for _ in range(N)] for _ in range(N)
    ]
    for i in range(N):
        dist[i][i] = 0
    for _ in range(M):
        a, b, c = read_ints()
        dist[a-1][b-1] = dist[b-1][a-1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = dist[j][i] = min(dist[i][j], dist[i][k]+dist[k][j])
    for i in range(N):
        for j in range(N):
            if i == j: continue
            dist[i][j] = 1 if dist[i][j] <= L else math.inf
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = dist[j][i] = min(dist[i][j], dist[i][k]+dist[k][j])
    Q = read_int()
    for _ in range(Q):
        s, t = read_ints()
        if dist[s-1][t-1] == math.inf:
            print(-1)
        else:
            print(dist[s-1][t-1]-1)


if __name__ == '__main__':
    solve()
