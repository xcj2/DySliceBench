import math
from typing import List, Counter, Tuple
from collections import Counter
from itertools import permutations


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


INF = 10**18

def knapsack(A: List[int], B: List[int], C: List[int], N: int, M: int):
    dp = [[-INF]*(M+1) for _ in range(N+1)]
    dp[0][0] = 0
    # dp[i][k] = max(dp[i-1][k], dp[i-1][k-1]+A[i]+B[i]+C[i])
    # dp[0][0] = 0
    for i in range(1, N+1):
        dp[i][0] = 0
        for j in range(1, M+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+A[i-1]+B[i-1]+C[i-1])
    return dp[N][M]


def solve() -> int:
    N, M = read_ints()
    A, B, C = [], [], []
    for _ in range(N):
        a, b, c = read_ints()
        A.append(a)
        B.append(b)
        C.append(c)
    max_score = -INF
    for a_sign in [-1, 1]:
        for b_sign in [-1, 1]:
            for c_sign in [-1, 1]:
                score = knapsack([a*a_sign for a in A],
                                 [b*b_sign for b in B],
                                 [c*c_sign for c in C],
                                 N, M)
                max_score = max(max_score, score)
    return max_score


if __name__ == '__main__':
    print(solve())
