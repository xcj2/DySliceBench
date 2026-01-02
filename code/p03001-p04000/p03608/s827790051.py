import itertools
import sys

def readline():
    return sys.stdin.readline()

def read_int_list():
    return list(map(int, readline().split()))

def read_int():
    return int(readline())

def main():
    N, M, R = map(int, input().split())
    r = map(int, input().split())

    inf = float("inf")
    d = [[inf] * (N + 1) for _ in range(N + 1)]
    for n in range(1, N + 1):
        d[n][n] = 0

    for _ in range(M):
        a, b, c = map(int, input().split())
        d[a][b] = c
        d[b][a] = c

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    min_cost = inf
    for p in itertools.permutations(r):
        cost = 0
        for i in range(len(p) - 1):
            src, dst = p[i:i + 2]
            cost += d[src][dst]
        min_cost = min(min_cost, cost)

    print(min_cost)


if __name__ == '__main__':
    main()
