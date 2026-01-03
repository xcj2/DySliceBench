import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, M = read_ints()
    dist = [
        [math.inf]*N for _ in range(N)
    ]

    for i in range(N):
        dist[i][i] = 0

    A, B, C = [], [], []
    for _ in range(M):
        a, b, c = read_ints()
        a -= 1
        b -= 1
        A.append(a)
        B.append(b)
        C.append(c)
        dist[a][b] = dist[b][a] = c

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][k]+dist[k][j], dist[i][j])

    count = M
    for i in range(M):
        is_shortest = False
        for j in range(N):
            if dist[j][A[i]] == dist[j][B[i]]+C[i]:
                is_shortest = True
        if is_shortest:
            count -= 1
    return count


if __name__ == '__main__':
    print(solve())
