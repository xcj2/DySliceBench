import sys
from functools import lru_cache
input = sys.stdin.readline
sys.setrecursionlimit(2 * 10**6)


def inpl():
    return list(map(int, input().split()))


def main():
    @lru_cache(maxsize=None)
    def recur(i, j):
        # print(i, j)
        if i == j:
            return 0
        for k in range(i, j):
            c = recur(i, k) + recur(k + 1, j) + P[i] * P[k + 1] * P[j + 1]
            if c < cost[i][j]:
                cost[i][j] = c
        return cost[i][j]

    N = int(input())
    RC = [inpl() for _ in range(N)]
    cost = [[float('inf')] * (N + 1) for a in range(N + 1)]
    P = [0] * (N + 1)
    for i, rc in enumerate(RC):
        P[i] = rc[0]
    P[N] = RC[N - 1][1]

    print(recur(0, N - 1))


if __name__ == '__main__':
    main()

