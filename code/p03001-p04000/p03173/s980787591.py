import math
from functools import lru_cache, reduce


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def prefix_sum(arr, a):
    arr.append(arr[-1]+a)
    return arr


def solve():
    """
    OPT[i][j] = min(OPT[i][k]+OPT[k+1][j])+sum(A[i:j+1])    i <= k < j
    OPT[i][j] = 0 if i == j
    """
    N = read_int()
    A = read_ints()
    prefix = reduce(prefix_sum, A, [0])

    @lru_cache(None)
    def dp(i, j):
        if i == j:
            return 0
        return min(dp(i, k)+dp(k+1, j)+(prefix[j+1]-prefix[i]) for k in range(i, j))

    OPT = [[0]*N for _ in range(N)]
    for j in range(N):
        for i in range(j-1, -1, -1):
            OPT[i][j] = min(OPT[i][k]+OPT[k+1][j] for k in range(i, j))+(prefix[j+1]-prefix[i])

    return OPT[0][N-1]


if __name__ == '__main__':
    print(solve())
